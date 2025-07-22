# Revision: Draft
# Date:     2025-07-22 10:59
# Notes:    Uses GitHub API for retreaving file contents.
#           It can be used on files smaller than 1 Mb

import base64
import json
import urllib.request

class reference:
    @classmethod
    def GetHttpText(cls,path):
        with urllib.request.urlopen(path) as response:
            return response.read().decode()
    @classmethod
    def GithubFile(cls,owner,repo,path):
        response = json.loads(cls.GetHttpText(f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"))
        b64content = response["content"]
        return base64.b64decode(b64content).decode('utf-8')

exec(reference.GithubFile("jesusjorge","pysite","index.py"), globals(), locals())
