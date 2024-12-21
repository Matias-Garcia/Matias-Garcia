import socket
from plyer import notification

# Get the local machine's IP address
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to send notification
def send_notification(ip):
    notification.notify(
        title="IP Address Notification",
        message=f"Your IP address is: {ip}",
        timeout=10  # Time in seconds the notification will be visible
    )

if __name__ == "__main__":
    ip = get_ip()
    send_notification(ip)
