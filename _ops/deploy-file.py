#!/usr/bin/env python3
"""Deploy a single file to BootCampFX GitHub Pages via the Contents API.

Use this instead of `git push` on Drago's box (osxkeychain blocks Bearer push).
Reads the token from /Users/macmini/github_token.rtf — RAW TEXT (ghp_…), NOT RTF,
so read it directly (open().read().strip()); textutil will fail on it.

Usage (from the local clone):
  cd /Users/macmini/sites/bootcampfx
  python3 _ops/deploy-file.py runner.html "commit message"
  python3 _ops/deploy-file.py mahjong/index.html "fix tiles" --live https://bootcampfx.com/mahjong/

Verifies: local MD5 == API blob MD5 (authoritative), then polls the live URL until
its MD5 matches (GitHub Pages + CDN lag 30–120s). Exits 0 on live confirmation.
"""
import urllib.request, base64, json, hashlib, sys, time, argparse

TOKEN_PATH = "/Users/macmini/github_token.rtf"
REPO = "curtisfx/bootcampfx"
LIVE_BASE = "https://bootcampfx.com"

def req(url, token, method="GET", payload=None):
    r = urllib.request.Request(url, method=method)
    r.add_header("Authorization", "Bearer " + token)
    r.add_header("Accept", "application/vnd.github+json")
    r.add_header("X-GitHub-Api-Version", "2022-11-28")
    body = None
    if payload is not None:
        body = json.dumps(payload).encode()
        r.add_header("Content-Type", "application/json")
    resp = urllib.request.urlopen(r, body)
    return resp.status, resp.read()

def live_url_for(path):
    """Map a repo-relative path to its served URL. index.html -> directory."""
    if path == "index.html":
        return LIVE_BASE + "/"
    if path.endswith("/index.html"):
        return LIVE_BASE + "/" + path[: -len("index.html")]
    return LIVE_BASE + "/" + path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="repo-relative path, e.g. runner.html or mahjong/index.html")
    ap.add_argument("message", nargs="?", default=None, help="commit message")
    ap.add_argument("--live", default=None, help="override live URL to poll")
    ap.add_argument("--no-poll", action="store_true", help="skip live polling")
    args = ap.parse_args()

    token = open(TOKEN_PATH).read().strip()  # plain text, not rtf
    api = "https://api.github.com/repos/%s/contents/%s" % (REPO, args.path)

    with open(args.path, "rb") as f:
        data = f.read()
    local_md5 = hashlib.md5(data).hexdigest()
    print("local md5:", local_md5)

    _, body = req(api, token)
    sha = json.loads(body)["sha"]
    print("current blob sha:", sha)

    msg = args.message or ("Update " + args.path)
    status, body = req(api, token, "PUT", {
        "message": msg,
        "content": base64.b64encode(data).decode(),
        "sha": sha,
    })
    res = json.loads(body)
    print("PUT", status, "commit", res["commit"]["sha"])

    # authoritative check: API blob (raw.githubusercontent.com can lag)
    _, body = req(api, token)
    blob = base64.b64decode(json.loads(body)["content"])
    api_md5 = hashlib.md5(blob).hexdigest()
    print("api blob md5:", api_md5, "match=", api_md5 == local_md5)

    if args.no_poll:
        return 0

    live_url = args.live or live_url_for(args.path)
    for i in range(6):
        try:
            live = urllib.request.urlopen(urllib.request.Request(
                live_url, headers={"User-Agent": "verify", "Cache-Control": "no-cache"})).read()
        except Exception as e:
            print("live attempt", i + 1, "error", e)
            time.sleep(20)
            continue
        m = hashlib.md5(live).hexdigest()
        print("live attempt", i + 1, "md5=", m, "match=", m == local_md5)
        if m == local_md5:
            print("LIVE CONFIRMED")
            return 0
        time.sleep(20)
    print("LIVE NOT YET PROPAGATED")
    return 1

if __name__ == "__main__":
    sys.exit(main())
