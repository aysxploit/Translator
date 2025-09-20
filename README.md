# 🌍 LinguaFlash  
**Translation API & UI — Powered by Python 3.13**

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)  
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green?style=for-the-badge&logo=fastapi)  
![Gradio](https://img.shields.io/badge/Gradio-4.44+-orange?style=for-the-badge&logo=gradio)  
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

A minimal, async-ready translation service with:  
🚀 FastAPI backend for API requests  
🎨 Gradio frontend for real-time UI  
⚡ Python 3.13 compatibility with structural pattern matching & Pydantic v2  

---

## ✨ Features
- `/translate/` API endpoint for text translations  
- Swagger + Redoc auto-generated documentation  
- Autodetect source language if not provided  
- Configurable via `.env`  
- Clean Gradio UI  

---

## 📂 Project Structure
```
Translator/
├── main.py             # FastAPI backend
├── app.py              # Gradio UI
├── requirements.txt    # Dependencies
├── .env.example        # Env template
└── README.md           # Documentation
```

---

## ⚡️ Quickstart

### 1. Clone Repository
```
git clone https://github.com/aysxploit/Translator
cd Translator
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Configure Environment
`.env` file:
```
TRANSLATION_API_URL=https://api.example.com/v1/translate
TRANSLATION_API_KEY=your_api_key_here
API_BASE_URL=http://127.0.0.1:8000
```

### 4. Start Backend
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- Swagger → http://localhost:8000/docs  
- Redoc → http://localhost:8000/redoc  

### 5. Start Frontend
```
python app.py
```
- UI → http://localhost:7860  

---

## 🛠️ Usage

### API Request
```
POST /translate/
```
```json
{
  "text": "Hello, world!",
  "target_language": "es",
  "source_language": "en"
}
```

### API Response
```json
{
  "translation": "¡Hola, mundo!",
  "detected_source_language": "en",
  "provider": "external-api"
}
```

### Gradio UI
1. Enter text  
2. Choose target language (`es`, `fr`, `de`)  
3. Leave source empty for autodetect or set manually  
4. Click **Translate**  

---

## 📦 Requirements
- Python 3.13+  
- fastapi ≥ 0.115  
- gradio ≥ 4.44  
- httpx ≥ 0.27  
- pydantic ≥ 2.9  
- uvicorn ≥ 0.30  
- python-dotenv ≥ 1.0  

---

## 🚀 Tech Highlights
- Async I/O with `httpx.AsyncClient`  
- Pattern Matching (`match/case`)  
- Pydantic v2 schema validation  
- Gradio Blocks UI  

---

## 📜 License
MIT License — free to use, modify, and distribute.
