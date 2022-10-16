from fastapi import FastAPI
from scrape import Scraper
import uvicorn

app = FastAPI()
tiktok = Scraper()

@app.get("/{username}")
async def userProfile(username):
    info = tiktok.scrape(username)
    return info

