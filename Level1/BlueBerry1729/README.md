# Installation steps done on Debian 11

1. **Enable Virtualization**

   **you can install virtualization by going into the system bios. This varies acc to system.**

2. **KVM virtualization support**

   ```bash
   modprobe kvm
   ```

    **Depending on the processor of the host machine, the corresponding module must be loaded:**

    ```bash
    modprobe kvm_intel  # Intel processors
    ```

    ```bash
    modprobe kvm_amd    # AMD processors
    ```

    **Set up KVM device user permissions**
    ```bash
     sudo usermod -aG kvm $USER

    ```

3. **For non-Gnome Desktop environments, gnome-terminal must be installed:**

     ```bash
     sudo apt install gnome-terminal
     ```

4. **Install Docker Desktop**

    **1. Download the latest [DEB package](https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64)**

    **2. Install the deb package**

    ```bash
    sudo apt-get update
    sudo apt-get install ./docker-desktop-(your architecture)).deb
    ```

5. **Signing in**

    **you will be asked to fill in your name and email. Do that.**

    ```bash
    gpg --generate-key
    ```

     ```bash
     pass init <your_generated_gpg-id_public_key>
     ```

6. **And now you are good to go!**
