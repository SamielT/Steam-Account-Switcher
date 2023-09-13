import subprocess
import sys

# Argument check
if len(sys.argv) != 2:
    print("Usage: python SteamAccSwitch.pyw <login_argument>")
    sys.exit(1)

login_argument = sys.argv[1]

# Define Steam executable path
steam_executable = r'C:\Program Files (x86)\Steam\Steam.exe'

# Close Steam
close_command = 'taskkill /f /im steam.exe'
close_process = subprocess.Popen(close_command, shell=True)
close_process.wait()  # Waiting for process to complete

# Construct
open_command = f'"{steam_executable}" -login {login_argument}'

# Subprocess run command
subprocess.Popen(open_command, shell=True)
