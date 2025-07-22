https://jesusjorge.github.io/

This is just my testing website


What I have here is a single line of code that can execute a Python Script, that is hosted in my other repository.

It also avoids any Cache Delay, since it [ab]uses GitHub API.

[Process Description]
1) bootstrap.py
    gets executed, it will fetch and execute...  
2) http://jesusjorge.github.io/autoexec.py
    This will call GitHub API in order to fetch and execute a script.
    Such API is...
3) https://api.github.com/repos/jesusjorge/pysite/contents/index.py
    This is the script I want to execute. It doesn't have any Cache Delay.
   
And all this can be executed from this individual line (Works with Linux and Windows)

```
python -c "exec(__import__('urllib.request').request.urlopen('http://jesusjorge.github.io/autoexec.py').read())"
```
