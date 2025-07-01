import os
import requests

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://localhost:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")
SECRET_PATH = os.getenv("SECRET_PATH", "secret/data/api_key")

def store_key_in_password_store(key: str) -> bool:
    print(f"Storing key in password store: {key}")

    if not VAULT_TOKEN:
        print("Vault token not provided.")
        return False

    headers = {
        "X-Vault-Token": VAULT_TOKEN
    }

    data = {
        "data": {
            "api_key": key
        }
    }

    try:
        response = requests.post(f"{VAULT_ADDR}/v1/{SECRET_PATH}", json=data, headers=headers)
        response.raise_for_status()
        print(f"Stored key in password store at {SECRET_PATH}")
        return True
    except requests.RequestException as e:
        print(f"Error storing key in password store: {e}")
        return False
