# app.py
# Gradio UI for Python 3.13
import asyncio
import httpx
import os
import gradio as gr

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "15"))

async def translate_async(text: str, target_language: str, source_language: str | None = None) -> str:
    url = f"{API_BASE_URL.rstrip('/')}/translate/"
    payload = {"text": text, "target_language": target_language}
    if source_language:
        payload["source_language"] = source_language

    async with httpx.AsyncClient(timeout=TIMEOUT_SECONDS) as client:
        resp = await client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json().get("translation", str(resp.json()))

def translate_sync(text: str, target_language: str, source_language: str | None = None) -> str:
    return asyncio.run(translate_async(text, target_language, source_language))

with gr.Blocks(title="LinguaFlash UI") as demo:
    gr.Markdown("# LinguaFlash — Translation App (Python 3.13)")
    with gr.Row():
        with gr.Column(scale=4):
            txt = gr.Textbox(label="Text", lines=6)
            source = gr.Textbox(label="Source language (optional)")
            target = gr.Textbox(label="Target language", value="es")
            btn = gr.Button("Translate")
        with gr.Column(scale=6):
            out = gr.Textbox(label="Translation", interactive=False, lines=6)
    btn.click(fn=translate_sync, inputs=[txt, target, source], outputs=[out])

if _name_ == "_main_":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)