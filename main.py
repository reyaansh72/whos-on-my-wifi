import subprocess
import re
import csv
import argparse
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# -----------------------------
# Load MAC vendors CSV
# -----------------------------
VENDOR_FILE = "oui.csv"  # path to your IEEE csv file
vendors = {}

with open(VENDOR_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prefix = row['Assignment'].upper().replace(':','').replace('-', '')
        vendors[prefix] = row['Organization Name']

# -----------------------------
# ARP scan
# -----------------------------
def get_arp_table():
    result = subprocess.run("arp -a", capture_output=True, text=True, shell=True)
    lines = result.stdout.splitlines()
    entries = []
    current_interface = None

    for line in lines:
        iface_match = re.match(r"Interface: ([0-9.]+) ---", line)
        if iface_match:
            current_interface = iface_match.group(1)
            continue

        arp_match = re.match(r"\s*([0-9.]+)\s+([0-9a-fA-F-]+)\s+(\w+)", line)
        if arp_match:
            ip = arp_match.group(1)
            mac = arp_match.group(2).upper().replace('-', ':')
            entries.append({
                'ip': ip,
                'mac': mac,
                'interface': current_interface
            })
    return entries

# -----------------------------
# Determine vendor
# -----------------------------
def lookup_vendor(mac):
    prefix = mac.replace(':','')[:6]
    return vendors.get(prefix, "Unknown")

# -----------------------------
# Detect junk/fake IPs
# -----------------------------
def is_junk_ip(ip):
    return (ip.startswith("224.") or ip.startswith("239.") or ip.startswith("169.254") or ip == "255.255.255.255")

# -----------------------------
# Display table
# -----------------------------
def display_table(entries, show_junk=False):
    print(Fore.GREEN + "="*70)
    print(f"{'IP':<17}{'MAC':<20}{'Vendor'}")
    print("-"*70)
    for e in entries:
        vendor = lookup_vendor(e['mac'])
        if is_junk_ip(e['ip']):
            if show_junk:
                print(Fore.RED + f"{e['ip']:<17}{e['mac']:<20}{vendor}")
        else:
            # add random hacky messages in gray
            if random.random() < 0.1:
                msg = random.choice(["[SCAN]", "[PING]", "[ARP]", "[CHECK]"])
                print(Fore.GREEN + f"{msg} {e['ip']:<17}{e['mac']:<20}{vendor}")
            else:
                print(Fore.GREEN + f"{e['ip']:<17}{e['mac']:<20}{vendor}")
    print(Fore.GREEN + "="*70)

# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Hacky LAN scanner")
    parser.add_argument("--show-junk", action="store_true", help="Show junk/broadcast IPs")
    parser.add_argument("--loop", action="store_true", help="Continuously refresh")
    args = parser.parse_args()

    while True:
        entries = get_arp_table()
        display_table(entries, show_junk=args.show_junk)
        if not args.loop:
            break
        # wait a bit with random hacky console noise
        time.sleep(5)
        print(Fore.GREEN + Style.DIM + f"[{random.choice(['SCAN','PING','ARP','CHECK','TRACE'])}] Refreshing table...\n")

if __name__ == "__main__":
    main()