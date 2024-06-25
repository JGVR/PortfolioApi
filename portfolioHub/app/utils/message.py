from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    text: str