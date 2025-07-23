import base64
import json
import urllib.request

try:
  tRequest = urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py")
  tResponse = tRequest.read()
  tJson = json.loads(tResponse)
  tContent = tJson["content"]
  tDecoded = base64.b64decode(tContent)
  exec(tDecoded)
except urllib.error.HTTPError as e:
  if e.code == 403:
    print("⚠️ GitHub API limit reached. Falling back to raw content.")
    tRequest = urllib.request.urlopen(f"https://raw.githubusercontent.com/jesusjorge/pysite/refs/heads/main/bootinit.py")
    tResponse = tRequest.read()
    exec(tResponse)
  else:
      raise
