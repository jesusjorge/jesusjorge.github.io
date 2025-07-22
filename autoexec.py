# Revision: Draft
# Date:     2025-07-22 10:59
# Notes:    Uses GitHub API for retreaving file contents.
#           It can be used on files smaller than 1 Mb

import base64
import json
import requests

class reference:
    @classmethod
    def GetHttpText(cls,path):
        return requests.get(path).text
    @classmethod
    def GithubFile(cls,owner,repo,path):
        result = json.loads(cls.GetHttpText(f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"))
        content = result["content"]
        return base64.b64decode(content).decode('utf-8')

exec(reference.GithubFile("jesusjorge","pysite","index.py"), globals(), locals())

