from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import json
import os
import tempfile

app = FastAPI(title="Neville's Remembrall Vault")

DATA_FILE = "vault.json"

class PasswordEntry(BaseModel):
    location: str = Field(..., min_length=1)
    hint: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)

# ---------- Storage Utilities ----------
def load_vault():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except:
        return []

def save_vault(vault):
    fd, temp_path = tempfile.mkstemp()
    with os.fdopen(fd, "w", encoding="utf-8") as tmp:
        json.dump(vault, tmp, indent=2)
    os.replace(temp_path, DATA_FILE)

# ---------- Routes ----------
@app.post("/add-password")
def add_password(entry: PasswordEntry):
    vault = load_vault()
    vault.append({
        "location": entry.location.strip(),
        "hint": entry.hint.strip(),
        "password": entry.password.strip()
    })
    try:
        save_vault(vault)
    except:
        raise HTTPException(status_code=500, detail="Storage failed")
    return {
        "success": True,
        "message": "Password stored successfully",
        "total": len(vault)
    }

@app.get("/get-hint-locations")
def get_hint_locations():
    vault = load_vault()
    return {
        "count": len(vault),
        "data": [
            {"location": v["location"], "hint": v["hint"]}
            for v in vault
        ]
    }

@app.delete("/clear-vault")
def clear_vault():
    save_vault([])
    return {"success": True, "message": "All passwords cleared"}

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
