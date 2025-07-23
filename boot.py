import base64
import json
import urllib.request
import urllib.error

try:
  tRequest = urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py")
  tResponse = tRequest.read()
  tJson = json.loads(tResponse)
  tContent = tJson["content"]
  tDecoded = base64.b64decode(tContent)
  print("Retrieving from https://api.github.com/")
  exec(tDecoded)
except urllib.error.HTTPError as e:
  if e.code == 403: #GitHub API rate limit exceeded. Don't panic, just use CDN.
    tRequest = urllib.request.urlopen(f"https://raw.githubusercontent.com/jesusjorge/pysite/main/bootinit.py")
    tResponse = tRequest.read()
    print("Retrieving from https://raw.githubusercontent.com/")
    exec(tResponse)
  else:
      raise
