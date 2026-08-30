#!/usr/bin/env python3
import urllib.request, base64, json, hashlib, subprocess, sys

# Extract token from RTF without printing it
def extract_token(path):
    with open(path) as f:
        return f.read().strip()

token = extract_token("/Users/macmini/github_token.rtf")
if not token:
    print("NO TOKEN")
    sys.exit(1)

repo = "curtisfx/bootcampfx"
path = "runner.html"
api = f"https://api.github.com/repos/{repo}/contents/{path}"

with open("runner.html", "rb") as f:
    content_bytes = f.read()

local_md5 = hashlib.md5(content_bytes).hexdigest()
print(f"local md5: {local_md5}")

def req(url, method="GET", data=None):
    r = urllib.request.Request(url, method=method)
    r.add_header("Authorization", f"Bearer {token}")
    r.add_header("Accept", "application/vnd.github+json")
    r.add_header("X-GitHub-Api-Version", "2022-11-28")
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        r.add_header("Content-Type", "application/json")
    resp = urllib.request.urlopen(r, body)
    return resp.status, resp.read().decode()

# Get current SHA
status, body = req(api)
info = json.loads(body)
sha = info["sha"]
print(f"current sha: {sha}")

# PUT new content
payload = {
    "message": "Update runner start-page tag: describe the game itself",
    "content": base64.b64encode(content_bytes).decode(),
    "sha": sha,
}
status, body = req(api, "PUT", payload)
res = json.loads(body)
print(f"PUT status: {status}")
print(f"new sha: {res['commit']['sha']}")

# Verify raw
raw = f"https://raw.githubusercontent.com/{repo}/main/{path}"
status, rawbody = req(raw)
raw_bytes = rawbody.encode()
raw_md5 = hashlib.md5(raw_bytes).hexdigest()
print(f"raw md5: {raw_md5}")
print(f"MATCH: {raw_md5 == local_md5}")

# Verify live
live_url = "https://bootcampfx.com/runner.html"
try:
    lr = urllib.request.Request(live_url, headers={"User-Agent": "verify"})
    live = urllib.request.urlopen(lr).read()
    live_md5 = hashlib.md5(live).hexdigest()
    print(f"live md5: {live_md5}")
    print(f"LIVE MATCH: {live_md5 == local_md5}")
    # confirm the new string is present and old is gone
    s = live.decode(errors="replace")
    print(f"new line present: {'A video game' in s}")
    print(f"old line gone: {'sweat session' not in s}")
except Exception as e:
    print(f"live check error: {e}")
