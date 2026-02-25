
import abc

class LlmPort(abc.ABC):
    
    @abc.abstractmethod
    def chat_minify(self, input_data):
        pass