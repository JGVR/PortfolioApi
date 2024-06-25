from langchain.callbacks.base import BaseCallbackHandler

class StreamingCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.content = ""

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.content += token