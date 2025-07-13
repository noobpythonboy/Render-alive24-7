import requests
import time

APP_URL = "https://all-bot-s5cb.onrender.com"

try:
    response = requests.get(APP_URL)
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%S')}: Pinged {APP_URL} - Status {response.status_code}")
except Exception as e:
    print(f"Error pinging: {e}")
