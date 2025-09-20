from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = FastAPI()

# Load the .env file
load_dotenv()

# Access the API token
api_token = os.getenv('api_key')

# Configure the generative AI model
genai.configure(api_key=api_token)
model = genai.GenerativeModel("gemini-1.5-flash")

# Define a Pydantic model for the request body
class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    try:
        payload = {
            "input": request.text,
            "target_language": request.target_language
        }

        response = model.generate_content(f"Translate '{request.text}' to {request.target_language} YOU MUST ONLY TYPE THE TRANSLATION if no translation available, type the closest indirect translation and with newline write: Note: this is a closest indirect translation")

        # Extract translation from the response
        translation = response.text

        return {"translation": translation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
