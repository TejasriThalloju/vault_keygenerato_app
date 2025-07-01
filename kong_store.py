import os
import requests

KONG_ADMIN_URL = os.getenv("KONG_ADMIN_URL", "http://localhost:8001")
CONSUMER_USERNAME = os.getenv("CONSUMER_USERNAME", "api-consumer")

def store_key_in_kong(key: str) -> bool:
    print(f"Storing key in Kong: {key}")
    try:
        consumer_url = f"{KONG_ADMIN_URL}/consumers/{CONSUMER_USERNAME}"
        response = requests.put(consumer_url, json={"username": CONSUMER_USERNAME})
        response.raise_for_status()

        key_auth_url = f"{KONG_ADMIN_URL}/consumers/{CONSUMER_USERNAME}/key-auth"
        response = requests.post(key_auth_url, json={"key": key})
        response.raise_for_status()

        print(f"Stored key in Kong for consumer {CONSUMER_USERNAME}")
        return True
    except requests.RequestException as e:
        print(f"Error storing key in Kong: {e}")
        return False
