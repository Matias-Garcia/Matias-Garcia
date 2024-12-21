import os
import subprocess
import time

def restart_wifi():
    print("Disabling WiFi adapter...")
    # Disable the WiFi interface
    os.system("networksetup -setairportpower en0 off")  # Assuming 'en0' is your WiFi interface

    time.sleep(5)  # Wait for 5 seconds

    print("Enabling WiFi adapter...")
    os.system("networksetup -setairportpower en0 on")  # Re-enable WiFi
    time.sleep(10)  # Wait for WiFi to reconnect

    print("WiFi adapter restarted. Connection should improve.")

def scan_wifi_networks():
    print("Scanning for available networks...")
    # Use the 'wdutil' tool to scan for WiFi networks
    result = subprocess.run(['wdutil', 'scan'], stdout=subprocess.PIPE)
    networks = result.stdout.decode('utf-8')
    print("Available networks:\n", networks)

if __name__ == "__main__":
    restart_wifi()
    scan_wifi_networks()
