# ⚠️ **Disclaimer:**  
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
> 
> All code provided here is for educational and informational purposes only.  
> You are solely responsible for how you use it.  
> **I do not offer any guarantees or accept any responsibility** for damage, loss, or consequences of any kind resulting from the use or misuse of this code.
>



https://jesusjorge.github.io/

This is just my testing website

---
Perhaps some of you may know how complicated it is to deliver Software to a end user, with all its dependencies, files, and everyhing. Specially in the case of Python, which requires some extra steps. Now imagine that you also need to update such software, so you will have to start the process again, doing reinstalls, and extra steps. 

Wouldn't it be nice if we could just send him one link, and just by clicking it, it will instantly install, configure, and run such software. Just **Click and Run**. And any updates don't require any user intervention. It will always run the latest update. Just in the same way as we could update a Website, and don't require the user to "reinstall" or setup anything. Just hands free software.



That would simplify most of the [Package Software] -> [Deliver to User] -> [User (re)install software] - > [User uses the software] -> [User requires changes] -> [Developer rewrites software] -> back to step 1, Package Software

It will turn that into this: [Developer writes software] -> [User uses the software] -> [User requires changes] -> back to step 1



What I have here is a single line of code that will result in a cascade of events that will lead to:
- Automatic pip installs when required
- Faster Access to files in GitHub repositories
- Execute a large Python program hosted in GitHub
- And all of that without any user installation, configuration, or intervention

It spares you of any user intervention. The only thing that the users needs is a computer with Python installed, and execute one single line of code, either in Console, Python REPL, or download start.py and run it.

It also tries to avoids Cache Delay, since it uses GitHub API. Such API has a [rate limit](https://api.github.com/rate_limit). It will fall back automatically to Raw GitHub CDN when it reaches it.

[Process Description]
1) **[START]** [start.py](https://github.com/jesusjorge/jesusjorge.github.io/blob/master/start.py) 100 byte(s), or a single line in Python or Console
    gets executed, it will fetch and execute...
   
2) **[BOOT]** [https://jesusjorge.github.io/boot.py](https://github.com/jesusjorge/jesusjorge.github.io/blob/master/boot.py) 760 byte(s)
    This will call [GitHub API](https://api.github.com/repos/jesusjorge/pysite/contents/init.py) in order to fetch and execute a script.
    If it fails, it will fallback to [raw GitHub CDN](https://raw.githubusercontent.com/jesusjorge/pysite/main/init.py)
   
3) **[INIT]** [https://github.com/jesusjorge/pysite/blob/main/init.py](https://github.com/jesusjorge/pysite/blob/main/init.py)  larger than 1 kilobyte(s)
    This is the script I want to execute. It doesn't have any Cache Delay (sometimes)
    It also provides static methods for retreiving further files, install imports, and execute code
    From there, it will continue with the execution of the desired program.

- Process
  ```mermaid
  graph TD
    Start --> Boot --> Init --> User_Program

---

And all this can be executed from this individual line (Works with Linux and Windows)

```
python -c "exec(__import__('urllib.request').request.urlopen('http://jesusjorge.github.io/boot.py').read())"
```

---

So, the reason why I'm doing this, is in order to "test" if I could actually achieve such goal, of easy to modify software, without having to worry about any packaging, delivering, reinstall, user interaction, and so on. I also want to be 100% sure that the user isn't running an old version of my software.

This is just a test, and I don't recomend you to implement such *dangerous* method as the one I'm using it. I'm still polishing all the details so I can guarantee that there won't be any issues.

The end goal is to cut as much time as possible from the process of building software for clients. Specially for the cases in which requirements change constantly, and we get a vast amount of different versions of such software. So, adapt to constant change, deliver as fast as possible, and hands free interaction from the user.
