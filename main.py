from fastapi import FastAPI, Request, HTTPException
from key_generator import generate_unique_key
from password_store import store_password, retrieve_password

app = FastAPI()

@app.get("/generate")
def generate():
    key = generate_unique_key()
    return {"key": key}

@app.post("/store/{password_id}")
def store(password_id: str, password: str = "default_pass"):
    result = store_password(password_id, password)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.get("/retrieve/{password_id}")
def retrieve(password_id: str):
    result = retrieve_password(password_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

