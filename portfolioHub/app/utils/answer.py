from dataclasses import dataclass
from .message import Message
from .question import Question
from typing import List, Any

@dataclass(frozen=True)
class Answer(Message):
    question: Question
    completed: bool

    @classmethod
    def from_chunks(cls, chunks: List[str], question: Question):
        answer = "".join(chunks)
        return cls(text=answer, question=question, completed=True)
    
    def serialize(self):
        return {
            "text": self.text,
            "question": self.question.text,
            "completed": str(self.completed)
        }