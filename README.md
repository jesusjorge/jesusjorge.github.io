# ⚠️ **Disclaimer:**  
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
> 
> All code provided here is for educational and informational purposes only.  
> You are solely responsible for how you use it.  
> **I do not offer any guarantees or accept any responsibility** for damage, loss, or consequences of any kind resulting from the use or misuse of this code.
>



https://jesusjorge.github.io/

This is just my testing website

What I have here is a single line of code that can execute a Python Script, that is hosted in my other repository.

It also avoids any Cache Delay, since it uses GitHub API.

[Process Description]
1) **[START]** start.py or a single line in Python or Console
    gets executed, it will fetch and execute...
   
2) **[BOOT]** http://jesusjorge.github.io/boot.py
    This will call GitHub API in order to fetch and execute a script.
    If it fails, it will fallback to raw GitHub CDN
    Such API is...
   
3) **[INIT]** https://api.github.com/repos/jesusjorge/pysite/contents/init.py
    This is the script I want to execute. It doesn't have any Cache Delay (sometimes)
    It also provides static methods for retreiving further files, install imports, and execute code
    From there, it will continue with the execution of the desired program.
---

### 🧠 Notes:
- Use `graph TD` for a top-down layout
  ```mermaid
  graph LR
    Start --> Boot --> Init --> Program



   
And all this can be executed from this individual line (Works with Linux and Windows)

```
python -c "exec(__import__('urllib.request').request.urlopen('http://jesusjorge.github.io/boot.py').read())"
```
