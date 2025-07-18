from fastapi import FastAPI
from tgtg import TgtgClient
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Optional: CORS middleware to allow external calls (e.g., from n8n or frontend apps)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider narrowing for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the TGTG client using environment variables
client = TgtgClient(
    access_token=os.getenv("TGTG_ACCESS_TOKEN"),
    refresh_token=os.getenv("TGTG_REFRESH_TOKEN"),
    cookie=os.getenv("TGTG_COOKIE")
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "TGTG API is running."}

@app.get("/")
def root():
    return {"status": "ok", "message": "Welcome to the TGTG API."}

@app.get("/check")
def check_items():
    try:
        items = client.get_items()
        return {
            "status": "ok",
            "count": len(items),
            "items": items,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
