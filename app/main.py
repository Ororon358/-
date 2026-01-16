from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from app.storage import URLStorage

app = FastAPI()
storage = URLStorage()

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
async def shorten_url(request: URLRequest):
    short_id = storage.create_short_url(request.url)
    return {"short_url": f"http://localhost:8000/{short_id}"}

@app.get("/{short_id}")
async def redirect_to_url(short_id: str):
    original_url = storage.get_original_url(short_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)

@app.get("/")
async def home():
    return {"message": "Welcome to URL Shortener! Use /shorten to create a short link."}
