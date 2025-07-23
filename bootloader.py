import base64, json, urllib.request
tResponse = urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py").read()
tJson = json.loads(tResponse)
tContent = tJson["content"]
tFromB64 = base64.b64decode(tContent)
exec(tFromB64)
