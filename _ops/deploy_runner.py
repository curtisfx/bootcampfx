#!/usr/bin/env python3
import urllib.request, base64, json, hashlib, sys, time

token = open("/Users/macmini/github_token.rtf").read().strip()
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

status, body = req(api)
sha = json.loads(body)["sha"]
print(f"current blob sha: {sha}")

payload = {
    "message": "Fix duck sprite shape in runner",
    "content": base64.b64encode(content_bytes).decode(),
    "sha": sha,
}
status, body = req(api, "PUT", payload)
res = json.loads(body)
print(f"PUT status: {status}, commit {res['commit']['sha']}")

# verify API blob
status, body = req(api)
blob = base64.b64decode(json.loads(body)["content"])
print(f"api blob md5: {hashlib.md5(blob).hexdigest()}  match={hashlib.md5(blob).hexdigest()==local_md5}")

# verify live (poll for GitHub Pages propagation)
for i in range(6):
    live = urllib.request.urlopen(urllib.request.Request("https://bootcampfx.com/runner.html", headers={"User-Agent":"verify","Cache-Control":"no-cache"})).read()
    m = hashlib.md5(live).hexdigest()
    print(f"live attempt {i+1}: md5={m} match={m==local_md5}")
    if m == local_md5:
        print("LIVE CONFIRMED")
        sys.exit(0)
    time.sleep(20)
print("LIVE NOT YET PROPAGATED")
sys.exit(1)
