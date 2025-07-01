import uuid
import secrets

def generate_unique_key(method: str = "uuid") -> str:
    if method == "uuid":
        return str(uuid.uuid4())
    elif method == "secrets":
        return secrets.token_urlsafe(32)
    else:
        raise ValueError("Unsupported key generation method")
