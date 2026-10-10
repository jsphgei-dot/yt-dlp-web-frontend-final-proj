from pathlib import Path
from urllib.parse import urlparse

import yt_dlp
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
ALLOWED_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtu.be"}

app = FastAPI()


@app.get("/api/info")
def info(url: str):
    if urlparse(url).hostname not in ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail="Only YouTube URLs are supported")

    try:
        with yt_dlp.YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
    except yt_dlp.utils.DownloadError as error:
        raise HTTPException(status_code=422, detail=str(error))

    return {
        "url": url,
        "title": info_dict.get("title"),
        "uploader": info_dict.get("uploader"),
        "duration": info_dict.get("duration"),
    }


app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")
