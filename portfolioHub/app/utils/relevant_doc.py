from dataclasses import dataclass

@dataclass(froze=True)
class RelevantDoc:
    content: str

    def serialize(self):
        return {
            "content": self.content
        }