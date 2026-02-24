import google.generativeai as genai
from src.config.settings import settings

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            # Aquí inyectaremos las herramientas (functions) más adelante
        )

    def start_conversation(self, tools: list):
        return self.model.start_chat(enable_automatic_function_calling=True, tools=tools)