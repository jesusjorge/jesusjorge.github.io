import base64
import json
import urllib.request
import urllib.error

try:
  tRequest = urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/init.py")
  tResponse = tRequest.read()
  tJson = json.loads(tResponse)
  tContent = tJson["content"]
  tDecoded = base64.b64decode(tContent)
  print("Retrieving from https://api.github.com/")
  exec(compile(tDecoded, "https://github.com/jesusjorge/pysite/blob/main/init.py", 'exec'))
except urllib.error.HTTPError as e:
  if e.code == 403: ##### GitHub API rate limit exceeded. Don't panic, use the contents from CDN #####
    tRequest = urllib.request.urlopen(f"https://raw.githubusercontent.com/jesusjorge/pysite/main/init.py")
    tResponse = tRequest.read()
    print("Retrieving from https://raw.githubusercontent.com/")
    exec(compile(tResponse, "https://github.com/jesusjorge/pysite/blob/main/init.py", 'exec'))
  else:
      raise
