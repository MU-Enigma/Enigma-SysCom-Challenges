

---

# Pop!_OS Rice Documentation

**By:** Parv Dubey  
**ID:** SE23UMEC021

## 1. Setting the Wallpaper
- **Method:** Open the Settings application.
- **Navigation:** Desktop → Background.
- **Wallpaper:** A custom wallpaper has been uploaded to the repository for reference.

## 2. Installing and Applying Themes
1. **Download Theme:**
   - Visit [GNOME-Look.org](https://www.gnome-look.org).
   - Navigate to **Gnome Shell Themes** on the left sidebar.
   - Select your desired theme, click on the **Files** tab under the preview image, and download (click the download icon, **not** the install button).
   
2. **Extract and Place Theme:**
   - Extract the downloaded `.zip` file.
   - Ensure all extracted folders contain a `.themes` file.
   - Open your File Manager, navigate to your home directory, create a folder named `.themes`, and paste the extracted folders there.

3. **Install GNOME Tweaks:**
   - **Via Software Center:** Search for and install **Gnome Tweaks**.
   - **Via Terminal:**
     - **For Ubuntu/Debian:**
       ```bash
       sudo apt update
       sudo apt install gnome-tweaks
       ```
     - **For Fedora/RHEL:**
       ```bash
       sudo dnf install gnome-tweaks
       ```
     - **For Arch-based:**
       ```bash
       sudo pacman -S gnome-tweaks
       ```

4. **Apply Theme:**
   - Open GNOME Tweaks, navigate to the **Appearance** tab, and select your downloaded theme.
   - **Theme Used:** [Link to Theme](https://www.gnome-look.org/p/2014493)

5. **Unlock Shell Customization:**
   - Download **Extension Manager** from your software center.
   - Search for **User Themes** by gcampax in Extension Manager, install and enable it.
   - This allows shell customization similar to theme application.

## 3. Custom Icons and Cursors
1. **Download Icons and Cursors:**
   - Navigate to [GNOME-Look.org](https://www.gnome-look.org).
   - Go to **Full Icon Themes** for icons and **Cursors** tab for cursors.

2. **Place Icons and Cursors:**
   - In your home directory, create a folder named `.icons`, and paste the extracted folders from the downloaded icon and cursor `.zip` files.

3. **Apply Icons and Cursors:**
   - Use the **Tweaks** application to apply the downloaded icons and cursors.

## 4. Installing Extensions for Desktop Customization
### Recommended Extensions:
- **Blur My Shell** (By aunetx): Adds a blur effect to the background when pressing the Applications tab.
- **Dash to Dock** (By micxgx): Customizes dock features such as opacity, size, color, and border limits.

### Recommended Extensions for Animation:
- **Compiz Window Effect** (By hermes83): Enhances window animations.
- **Magic Lamp Effect** (By hermes83): Provides drag/minimize/maximize animations.
- **Desktop Cube** (By schneegans): Adds cube transition effects when switching desktops/workspaces (suitable for mid to high-range PCs).
- **Burn My Windows** (By schneegans): Adds closing and opening animations to applications (animation used: Matrix).

## 5. Installing and Customizing Fonts
### System Fonts:
1. **Download Font:**
   - Head to [Google Fonts](https://fonts.google.com) and download your desired font (used: **Slabo27px**).

2. **Install Font:**
   - Extract the font from the `.zip` file.
   - Double-click the font folder and install it.

3. **Apply Font:**
   - Open the Tweaks application and select the font under the **Fonts** tab (do not apply to Monospace).

### Terminal Fonts:
1. **Download Monospace Font:**
   - Use the Monospace filter on Google Fonts to select and download a font of your liking.

2. **Apply Monospace Font:**
   - Open your terminal, click the menu button, then **Preferences**.
   - Under **Profiles**, select your profile and set the font we just downloaded.

## 6. Customizing the Default Terminal
1. **Access Terminal Preferences:**
   - Click the menu button in your terminal and select **Preferences**.
   - Under **Profiles**, choose your profile.

2. **Customize Cursor and Colors:**
   - **Cursor:**
     - Change cursor shape to **I-beam**.
     - Disable cursor blinking.
   - **Colors:**
     - Uncheck **Use colors from system theme**.
     - Uncheck **Bold color**.
     - Ensure **Cursor color** is checked.
     - Set **Highlight second color** to red.
     - Set background transparency to 10 pts.
     - Set **Palette** to **Custom**.
     - Check **Show bold text in bright colors**.

3. **Scrolling:**
   - Uncheck **Show scrollbar**.
   - Uncheck **Scroll on output** (keep remaining options checked).

## 7. Installing Kitty Terminal
1. **Install Kitty:**
   - Run the following command in your terminal:
   ```bash
   curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin
   ```

2. **Install Kitty via Package Manager:**
   - Based on your distro:
     - **For Ubuntu:**
       ```bash
       sudo apt install kitty
       ```

3. **Open Kitty and Install Neofetch:**
   - Run:
   ```bash
   sudo apt install neofetch
   ```

4. **Customize Kitty:**
   - Press `Ctrl+Shift+F2` to open `kitty.conf` in **vim**.
   - Set the following:
     - **Font:** `FiraCode Nerd Font Mono`
     - **Font Size:** `15`
     - **Background Image:** Set the path in the `background_image` function.
     - **Background Image Layout:** Set to `scaled`.
     - **Background Tint:** Set to `0.5`.
     - **Margin Widths:**
       - `single_window_margin_width` to `0`.
       - `window_border_width` to `2pt`.
       - `window_margin_width` to `5`.
     - **Active Border Color:** Change to `#00ffff`.
     - **Tab Bar Style:** Set to `powerline`.
     - **Tab Powerline Style:** Set to `slanted`.

## Notes
- **GNOME Customization:** Gnome doesn't offer as much customizability as KDE Plasma, hence the use of Extensions and Tweaks.
- **Vim Tips:** To search in vim, press `Esc`, then `/` and type your query.
- **Performance Warning:** Some extensions may require mid to high-range hardware. If you experience freezing, press `Alt + F2`, type `r`, and hit enter to restart the GNOME shell.

---
