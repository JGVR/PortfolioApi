from dataclasses import dataclass
from .message import Message

@dataclass(frozen=True)
class Question(Message):
    pass