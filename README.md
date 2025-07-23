[good](https://github.com/jesusjorge/jesusjorge.github.io/)

[bad](https://github.com/jesusjorge/jesusjorge.github.io/)

[ugly](https://jesusjorge.github.io/)

# ⚠️ **Disclaimer:**  
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
> 
> All code provided here is for educational and informational purposes only.  
> You are solely responsible for how you use it.  
> **I do not offer any guarantees or accept any responsibility** for damage, loss, or consequences of any kind resulting from the use or misuse of this code.
>





---
# Click & Boom 💣
Faster Process, Fewer Steps, Less Friction
![Fast](fast.jpg)

## ~Coding~ Programming ~amid~ Under ~Constant~ Frequent ~Requirement~ Needs ~Changes~ Updates
### Is that even possible?


Perhaps some of you know how complicated it is to deliver software to an end user, with all its dependencies, files, and everything. Especially in the case of Python, which requires some extra steps. Now imagine that you also need to update such software, you'd have to start the process again: reinstalls, extra steps, more friction.

![Complicated](complicated.avif)

Wouldn't it be nice if we could just send one link, and by clicking it, the software would instantly install, configure, and run? Just Click and Run. And updates? They wouldn't require any user intervention. It would always run the latest version, just like a website that updates without the user needing to reinstall or configure anything. Truly hands free software.

![Simple](simple.jpg)

That would simplify the whole:

>    [Package Software] → [Deliver to User] → [User (re)installs Software] → [User uses the software] → [User requests changes] → [Developer rewrites software] → back to step 1

into this:

>    [Developer writes software] → [User uses the software] → [User requests changes] → back to step 1

What I have here is a single line of code that triggers a cascade of actions:
- Automatically installs pip dependencies (if needed)
- Speeds up file access from GitHub repositories
- Executes a large Python program hosted on GitHub
- All without any installation, configuration, or manual steps from the user

It removes any need for user intervention. The only requirement is a computer with Python installed. The user just runs one line of code, either in the console, Python REPL, or by downloading and executing start.py.

![start](start.jpg)

It also tries to avoid cache delays by using the GitHub API. This API has a [rate limit](https://api.github.com/rate_limit), so the script will automatically fall back to the Raw GitHub CDN when needed.

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
And all this could (please don't) be executed from this individual line (Works with Linux and Windows)

```
python -c "exec(__import__('urllib.request').request.urlopen('http://jesusjorge.github.io/boot.py').read())"
```
And this is what it [looks like](https://github.com/jesusjorge/jesusjorge.github.io/blob/master/demo.png)

---

So why am I doing this?

Just to test whether it's possible to achieve that goal: easily updatable software, no packaging headaches, no delivery steps, no reinstalling, and no user configuration. I also want to make sure the user is always running the latest version of the code.

This is just a test, and I don’t recommend using this dangerous method in production (yet). I’m still polishing all the details so I can guarantee there won’t be any issues.

![testing](testing.jpg)

The end goal is to cut down development time when delivering software to clients, specially in cases where requirements change constantly, and multiple versions pile up. The goal is simple: adapt fast, deliver instantly, and eliminate all unnecessary user interaction.

![user friendly](userfriendly.png)

https://jesusjorge.github.io/

### ☯️ Well, if all this sounds good, what could possibly go wrong?

You can read about that here 

https://github.com/jesusjorge/pysite


