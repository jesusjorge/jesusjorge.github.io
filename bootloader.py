import base64, json, urllib.request
exec(base64.b64decode(json.loads(urllib.request.urlopen(f"https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py").read())["content"]))

# It retrives the contents of: https://api.github.com/repos/jesusjorge/pysite/contents/bootinit.py
# Parses it from JSON to Python Dict
# Looks for the item "content" and gets its value
# Converts such value from base64 to string
# Execute such string as Python Code

# This avoids any update delay, from GitHub CDN Cache.
# Fetching a file using Github API doesn't have that update delay issue
