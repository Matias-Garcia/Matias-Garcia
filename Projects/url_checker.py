import requests
import base64

# VirusTotal API setup
VIRUSTOTAL_API_KEY = ""  # Replace with your actual API key
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/urls"

def encode_url(url):
    """Encode the URL to Base64 as required by VirusTotal API."""
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def analyze_url(url):
    """Analyze a URL using the VirusTotal API."""
    encoded_url = encode_url(url)
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(f"{VIRUSTOTAL_URL}/{encoded_url}", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
        if malicious > 0:
            print(f"ALERT: The URL '{url}' is considered malicious with {malicious} reports.")
        else:
            print(f"The URL '{url}' is clean and safe.")
    else:
        print(f"Error: Unable to analyze the URL. Status code {response.status_code}")

def main():
    url = input("Enter the URL to analyze: ")
    analyze_url(url)

if __name__ == "__main__":
    main()
