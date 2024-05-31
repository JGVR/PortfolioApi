from langchain_community.chat_message_histories import ChatMessageHistory
from dataclasses import dataclass
from .message import Message
from .question import Question
from typing import List, Any

@dataclass(frozen=True)
class Answer(Message):
    question: Question
    chat_history: ChatMessageHistory
    completed: bool

    @classmethod
    def from_chunk(cls, chunks: List[str], question: Question, chat_history: ChatMessageHistory):
        answer = "".join(chunks)
        return cls(text=answer, question=question, complete=True)
    
    def serialize(self):
        return {
            "text": self.text,
            "question": self.question.text,
            "history": self.chat_history.messages,
            "complete": self.completed
        }