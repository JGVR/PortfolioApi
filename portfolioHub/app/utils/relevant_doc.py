from dataclasses import dataclass

@dataclass(frozen=True)
class RelevantDoc:
    content: str

    def serialize(self):
        return {
            "content": self.content
        }