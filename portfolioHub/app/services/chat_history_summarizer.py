from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate

@dataclass(frozen=True)
class ChatHistorySummarizer:
    llm: ChatOpenAI

    def call(self, chat_history: ChatMessageHistory) -> str:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "system prompt. ChatHistory: {chat_history}")
            ]
        )
        chain = prompt | self.llm
        result = chain.invoke({"chat_history": chat_history}).content
        return result