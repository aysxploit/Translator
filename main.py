# main.py code
# Compatible with Python 3.13 (pattern matching, type hints, async context managers)

from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, HttpUrl
import httpx
import os
import asyncio

class Settings(BaseModel):
    TRANSLATION_API_URL: HttpUrl = Field(..., alias="TRANSLATION_API_URL")
    TRANSLATION_API_KEY: str = Field(..., alias="TRANSLATION_API_KEY")
    TIMEOUT_SECONDS: int = 20

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            TRANSLATION_API_URL=os.environ["TRANSLATION_API_URL"],
            TRANSLATION_API_KEY=os.environ["TRANSLATION_API_KEY"],
            TIMEOUT_SECONDS=int(os.getenv("TIMEOUT_SECONDS", 20)),
        )

settings = Settings.from_env()

app = FastAPI(
    title="LinguaFlash (FastAPI)",
    version="1.0.0",
    description="Translation API wrapper (async, Python 3.13)."
)

class TranslateRequest(BaseModel):
    text: str
    target_language: str
    source_language: Optional[str] = None

class TranslateResponse(BaseModel):
    translation: str
    detected_source_language: Optional[str] = None
    provider: str = "external-api"

async def call_translation_api(payload: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {settings.TRANSLATION_API_KEY}",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=settings.TIMEOUT_SECONDS) as client:
        resp = await client.post(str(settings.TRANSLATION_API_URL), json=payload, headers=headers)
        if resp.is_error:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Provider error: {resp.text}")
        return resp.json()

@app.post("/translate/", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text must not be empty")

    payload = {"input": req.text, "target_language": req.target_language}
    if req.source_language:
        payload["source_language"] = req.source_language

    try:
        result = await call_translation_api(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"internal error: {e}")

    # Structural pattern matching (Python 3.10+ feature)
    match result:
        case {"translation": str(trans)}:
            translation = trans
        case {"translatedText": str(trans)}:
            translation = trans
        case {"data": {"translation": str(trans)}}:
            translation = trans
        case _:
            translation = str(result)

    detected = result.get("detected_source_language") or result.get("detectedLanguage")
    return TranslateResponse(translation=translation, detected_source_language=detected)

@app.get("/health")
async def health():
    return {"status": "ok"}