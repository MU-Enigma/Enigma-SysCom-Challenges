# Standard "Hello World" Docker (PS 1.1)

**By**: Parv Dubey  
**ID**: SE23UMEC021  

---

Due to Diwali holidays…I left my Linux laptop in hostel, so my level 1 and level 2 contributions have been done via my Windows laptop.

The files and softwares required for my Docker contribution are: 
- Windows 10 or 11
- Docker Desktop: Can be downloaded from here for Windows [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- VSCode
- Docker extension in VSCode for full compatibility

Now, setting up and running the Docker Desktop is very easy, just run the `.exe` file and follow all the on-screen commands. Ensure that the Docker Desktop is running by checking the system tray icons and locating the Docker Desktop icon there.

After that, head over to the **Settings** in Docker Desktop, and under the **General** tab, make sure that **WSL 2** is configured for the backend. Then restart the Docker Desktop. With that, your Docker Desktop is ready.

Install Visual Studio Code or any IDE for that matter.  
In case of VSCode, download the Docker extension from the extensions tab for compatibility with Docker Desktop.

To verify the installation of Docker Desktop:
- Open a new terminal in VSCode (or your own IDE) and run the command:
  ```bash
  docker --version
- Once the installation has been verified, run the following command
  ```bash
     docker run hello-world
- Docker will download the image (if not downloaded already) and run it
- You will see a message saying “Hello from Docker!”
  
