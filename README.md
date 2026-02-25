# 🟢 Hacky LAN Scanner

A terminal-based LAN scanner for Windows that lists live devices on your network.  
Real devices appear in **green**, while junk/fake IPs appear in **red**.  
Scan modes include clean-only or full (with junk IPs), and you can loop scans automatically.  

Everything runs from `main.py` and is launched via `start.bat`.

---

## ⚠️ Disclaimer

This tool is intended for **educational and personal network monitoring purposes only**.

You must **only use this scanner on networks you own or have explicit permission to scan**.

Unauthorized network scanning may violate laws, regulations, or your network provider’s terms of service.  
The author is **not responsible for misuse** of this software.

---

## Features

- ✅ Scan your local network and list all connected devices  
- ✅ Shows **IP**, **MAC**, and **Vendor** for each device  
- ✅ Differentiates **real devices** (green) vs **junk/fake IPs** (red)  
- ✅ Hacky, green terminal UI  
- ✅ Two scan modes selectable from `start.bat`:
  - **Clean Scan**: Only real devices  
  - **Full Scan**: Includes junk IPs and supports looped scanning  

---

## Requirements

- Windows 10+  
- Python 3.13+  
- Npcap installed (WinPcap compatible mode recommended)  
- Command Prompt (Administrator recommended)

---

## Installation

1. Download or extract the project folder.  
2. Ensure Python 3.13+ is installed and added to PATH.  
3. Install Npcap for Windows (enable WinPcap compatible mode).  

---

## Usage

Run the launcher:

```bat
start.bat