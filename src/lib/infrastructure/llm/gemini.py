from google import genai
from src.config.settings import settings

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
            
            )
        self.model_id = settings.GEMINI_MODEL
        self.system_prompt = """
        Eres el asistente oficial de Codenti.
        Reglas de oro:
        - Saluda de forma profesional.
        - Si no sabes algo de los productos, pide el email para contacto humano.
        - Usa emojis de forma moderada para ser amigable.
        - Prioriza soluciones técnicas basadas en .NET y MySQL.
        """
        
    def chat_minify(self, user_message: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                temperature=0.7 
            )
        )
        return response.text

    def start_conversation(self, tools: list):
        """
        Inicia un chat con herramientas (Function Calling)
        """
        # 4. Ahora se usa el manager de 'chats'
        return self.client.chats.create(
            model=self.model_id,
            config={'tools': tools}
        )