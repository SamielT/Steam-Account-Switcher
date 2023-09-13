# Steam Account Switcher

A Python script that allows you to quickly switch between Steam accounts.

## Prerequisites

- Python 3
- Steam
- Previously logged into the Steam account you intend to use with this script using the "Remember me" option.
- Correct Steam install path (if not in the default install path)

  To edit, open the `SteamAccSwitch.pyw` script in a text editor and locate the following line:

  ```python
  steam_executable = r'C:\Program Files (x86)\Steam\Steam.exe'
  ```
  Make sure that the steam_executable variable points to the correct path where Steam is installed on your system. If Steam is installed in a different location, update this line accordingly.

## Usage

You can use this script to quickly switch between Steam accounts in two ways:

**1. Command Line:**

   To switch between accounts using the command line, run the following command, replacing `<login_username>` with your Steam account's username:

   ```bash
   python SteamAccSwitch.pyw <login_username>
   ```

**2. Shortcut:**

   An alternative and convenient method is to create a desktop shortcut that allows you to switch between Steam accounts with a simple double-click. Here's how:

   - Locate the `SteamAccSwitch.pyw` script on your system.
   - Right-click on the script and select "Create shortcut."
   - Move the shortcut to your desktop or any other convenient location.
   - Rename the shortcut to something recognizable, like the name of account you're attempting to switch to.

   In the shortcut properties, navigate to the "Target:" field and add your login username after the script location, just like using the command line:
   ```bash
   "C:\Location\of\Script\SteamAccSwitch.pyw" <login_username>
   ```
