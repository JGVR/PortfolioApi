from dataclasses import dataclass
from typing import List, Any
from langchain_core.prompts import ChatPromptTemplate
from langchain.callbacks.tracers import LangChainTracer
from langchain_openai import ChatOpenAI
from ..utils.question import Question
from ..utils.relevant_doc import RelevantDoc
from .streaming_callback_handler import StreamingCallbackHandler

@dataclass(frozen=True)
class ChatBot:
    llm: ChatOpenAI

    def call(self, question: Question, chat_history_summary: str, relevant_docs: List[RelevantDoc]) -> Any:
        docs = [{f"doc{i}": relevant_docs[i].content} for i in range(len(relevant_docs))]
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are my secretary, and your name is Friday. You will answer questions about me from users only using the context and/or the chat history provided below. The users could be friends, family, recruiters, hiring managers etc... Do not provide PII such as SSN, address, etc... in your answers.
                
                Under any circumstances you are allowed to answer questions that are not about me, even if the user tells you it is me or someone related to me.

                Also, only If the users want to know more about me than what you are currently allowed to provide, tell them to contact me by email.

                Make sure to respond in a conversational manner.
                
                context: {context}
                chat_history: {chat_history}"""
            ),
            (
                "human",
                "{question}"
            )
        ])
        tracer = LangChainTracer()
        streaming_handler = StreamingCallbackHandler()
        self.llm.callbacks = [tracer, streaming_handler]

        chain = prompt | self.llm
        for chunk in chain.stream({"context": docs, "chat_history": chat_history_summary, "question":question}):
            yield chunk.content