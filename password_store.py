import os
import hvac

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://vault:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "root")

def store_password(password_id: str, password: str):
    try:
        client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

        if not client.is_authenticated():
            raise Exception("Vault auth failed")

        path = f"myapp_passwords/{password_id}"
        client.secrets.kv.v2.create_or_update_secret(
            path=path,
            secret={"password": password}
        )
        return {"message": f"Password stored under ID: {password_id}"}

    except Exception as e:
        return {"error": f"Vault error: {str(e)}"}

def retrieve_password(password_id: str):
    try:
        client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

        if not client.is_authenticated():
            raise Exception("Vault auth failed")

        path = f"myapp_passwords/{password_id}"
        response = client.secrets.kv.v2.read_secret_version(path=path)
        password = response["data"]["data"]["password"]

        return {"password_id": password_id, "password": password}

    except Exception as e:
        return {"error": f"Vault retrieval failed: {str(e)}"}

