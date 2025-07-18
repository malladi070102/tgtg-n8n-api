from fastapi import FastAPI
from tgtg import TgtgClient
import os

app = FastAPI()

# Initialize the TGTG client from environment variables
client = TgtgClient(
    access_token=os.getenv("TGTG_ACCESS_TOKEN"),
    refresh_token=os.getenv("TGTG_REFRESH_TOKEN"),
    cookie=os.getenv("TGTG_COOKIE")
)

@app.get("/")
def root():
    return {"status": "ok", "message": "TGTG API is running."}

@app.get("/check")
def check_items():
    try:
        items = client.get_items()
        return {"count": len(items), "items": items}
    except Exception as e:
        return {"error": str(e)}

