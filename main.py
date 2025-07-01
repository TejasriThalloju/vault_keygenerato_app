from dotenv import load_dotenv
load_dotenv()

from key_generator import generate_unique_key
from password_store import store_key_in_password_store
from kong_store import store_key_in_kong

def main():
    key = generate_unique_key("secrets")
    print(f"Generated Key: {key}")

    print("Storing in Vault...")
    success_store = store_key_in_password_store(key)
    print(f"Vault store result: {success_store}")

    print("Storing in Kong...")
    success_kong = store_key_in_kong(key)
    print(f"Kong store result: {success_kong}")

    print({
        "key": key,
        "vault_stored": success_store,
        "kong_stored": success_kong
    })

if __name__ == "__main__":
    main()
