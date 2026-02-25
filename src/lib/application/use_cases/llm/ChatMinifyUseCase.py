from src.lib.application.ports.llm_port import LlmPort


class ChatMinifyUseCase:
    def __init__(self, llm_port: LlmPort):
        self.llm_port = llm_port

    def execute(self, message: str):
        return self.llm_port.chat_minify(message)