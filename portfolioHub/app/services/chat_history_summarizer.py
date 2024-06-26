from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain.callbacks.tracers import LangChainTracer

@dataclass(frozen=True)
class ChatHistorySummarizer:
    llm: ChatOpenAI

    def call(self, chat_history: ChatMessageHistory) -> str:
        messages = [{message.type: message.content} for message in chat_history.messages]
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system", 
                    """I want you to summarize a conversation between an AI model and a user. Make sure to include key points of the conversation. I want you to summarize the conversation in a conversational manner.
                    
                    If there is no previous conversation, then just say "No previous conversation available" """
                ),
                (
                    "human",
                    "ChatHistory: {chat_history}"
                )
            ]
        )
        chain = prompt | self.llm
        tracer = LangChainTracer()
        result = chain.invoke({"chat_history": messages}, config={"callbacks": [tracer]}).content
        return result