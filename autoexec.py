import base64
import json
import urllib.request

class R1:
    
    @classmethod
    def GetHttpText(cls,path):
        with urllib.request.urlopen(path) as response:
            return response.read().decode()
            
    @classmethod
    def GithubFile(cls,owner,repo,path):
        response = json.loads(cls.GetHttpText(f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"))
        b64content = response["content"]
        return base64.b64decode(b64content).decode('utf-8')
        
exec(R1.GithubFile("jesusjorge","pysite","index.py"), globals(), locals())
