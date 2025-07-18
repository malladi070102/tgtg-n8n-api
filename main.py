from fastapi import FastAPI
from tgtg import TgtgClient
import os

app = FastAPI()

# Replace with your actual credentials or set them as environment variables
client = TgtgClient(
    access_token=os.getenv("TGTG_ACCESS_TOKEN"),
    refresh_token=os.getenv("TGTG_REFRESH_TOKEN"),
    user_id=os.getenv("TGTG_USER_ID"),
    cookie=os.getenv("TGTG_COOKIE")
)

@app.get("/check_food")
async def check_food():
    items = client.get_items()
    return {"items": items}
