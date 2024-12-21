import os
import platform
import subprocess

def ping_ip(ip_address, count=4):
    """
    Pings an IP address and returns the result.
    
    Args:
        ip_address (str): The IP address to ping.
        count (int): Number of ping attempts. Default is 4.
    
    Returns:
        str: The output of the ping command.
    """
    # Determine the ping command based on the operating system
    if platform.system().lower() == "windows":
        cmd = ["ping", "-n", str(count), ip_address]
    else:
        cmd = ["ping", "-c", str(count), ip_address]

    try:
        # Execute the ping command
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed with error:\n{e.output}"

if __name__ == "__main__":
    ip = input("Enter the IP address to ping: ").strip()
    count = input("Enter the number of pings (default is 4): ").strip()

    # Use default count if no input is provided
    count = int(count) if count.isdigit() else 4

    print(f"Pinging {ip} with {count} attempts...")
    result = ping_ip(ip, count)
    print("\nPing Result:\n")
    print(result)
