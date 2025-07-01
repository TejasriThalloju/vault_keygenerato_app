import os
import secrets
import hvac

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://vault:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "root")

def generate_unique_key():
    try:
        client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

        if not client.is_authenticated():
            raise Exception("Vault authentication failed")

        response = client.secrets.kv.read_secret_version(path="myapp")
        return response["data"]["data"]["SECRET_KEY"]

    except Exception as e:
        print(f"[Vault error] {e}")
        return secrets.token_urlsafe(32)

