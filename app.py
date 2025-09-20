import gradio as gr
import requests

def translate(text, target_language):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/translate/",
            json={"text": text, "target_language": target_language}
        )

        if response.status_code == 200:
            return response.json().get("translation")
        else:
            return "Translation failed"
    except Exception as e:
        return str(e)

iface = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text to translate..."),
        gr.Textbox(lines=1, placeholder="Enter target language (e.g., 'en', 'es', 'fr', etc.)")
    ],
    outputs=gr.Textbox(lines=2, placeholder="Translation appears here..."),
    title="Real-Time Language Translation Tool",
    description="Translate text from one language to another using Google Gemini 1.5 Flash.",
    live=False
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
