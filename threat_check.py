#!/usr/bin/env python3
import os
import time
import random
import subprocess
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# Function to read sudo failed attempts from journalctl
def get_failed_sudo_attempts():
    try:
        output = subprocess.check_output(
            "journalctl _COMM=sudo | grep 'authentication failure' | wc -l",
            shell=True, text=True
        )
        return int(output.strip())
    except:
        return 0

# Simulated metrics for other detections
def get_intrusion_attempts():
    return random.randint(0, 5)

def get_malware_detections():
    return random.randint(0, 3)

def get_ransomware_alerts():
    return random.randint(0, 1)

def get_phishing_attempts():
    return random.randint(0, 4)

def get_suspicious_logins():
    return random.randint(0, 2)

def get_lateral_movements():
    return random.randint(0, 1)

# Main hacker dashboard loop
def hacker_dashboard():
    while True:
        os.system("clear")

        # Title
        print(Fore.GREEN + Style.BRIGHT + "═" * 60)
        print(Fore.CYAN + Style.BRIGHT + "   REAL-TIME CYBERSECURITY THREAT MONITORING DASHBOARD   ")
        print(Fore.GREEN + Style.BRIGHT + "═" * 60)

        # Timestamp
        print(Fore.YELLOW + f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Live metrics
        print(Fore.RED + f"[!] Intrusion Attempts:      {get_intrusion_attempts()}")
        print(Fore.MAGENTA + f"[!] Malware Detections:     {get_malware_detections()}")
        print(Fore.LIGHTRED_EX + f"[!] Ransomware Alerts:      {get_ransomware_alerts()}")
        print(Fore.LIGHTMAGENTA_EX + f"[!] Phishing Attempts:      {get_phishing_attempts()}")
        print(Fore.BLUE + f"[!] Suspicious Logins:      {get_suspicious_logins()}")
        print(Fore.LIGHTBLUE_EX + f"[!] Lateral Movement:       {get_lateral_movements()}")

        # Real sudo failures
        print(Fore.LIGHTYELLOW_EX + f"[!] Failed sudo Attempts:   {get_failed_sudo_attempts()}")

        # Bottom hacker effect
        print(Fore.GREEN + "\n" + "█" * 60)
        print(Fore.LIGHTGREEN_EX + "   Monitoring in progress... Press CTRL+C to stop")
        print(Fore.GREEN + "█" * 60)

        time.sleep(2)

if __name__ == "__main__":
    try:
        hacker_dashboard()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Monitoring stopped.")
