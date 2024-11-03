1. I installed Docker from [docker.com](https://www.docker.com/).

2. I encountered the following problems:
   1. After installation, when I opened the app, it showed that the Docker engine was stopped.
   2. I navigated to Windows Security → App and browser control → Exploit protection settings → Program settings → vmcompute.exe → Control flow guard, turned it off by overriding the system settings, and then clicked "Apply."

3. After making these changes, Docker started working.

4. I opened Windows PowerShell and ran the command `docker run hello-world`.
