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

What I have here is a single line of code that will result in a cascade of events that will lead to:
- Automatic pip installs when required
- Faster Access to files in GitHub repositories
- Execute a large Python program hosted in GitHub
- And all of that without any user installation, configuration, or intervention

You could just get into a fresh Windows/Linux machine, with Python installed, and it will run the Python Script with all its dependencies, in the least amount of user effort.

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
