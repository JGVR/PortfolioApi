from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from ..utils.question import Question
from langchain_core.prompts import ChatPromptTemplate
from langchain.callbacks.tracers import LangChainTracer

@dataclass(frozen=True)
class FollowUpQuestionBuilder:
    llm: ChatOpenAI

    def call(self, question: Question, chat_history_summary: str) -> Question:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system", 
                    """Given the conversation history and a follow-up question, rephrase the follow-up question to make it a standalone question.
                    
                    Conversation History:
                    {chat_history}
                    Standalone Question:"""),
                 (
                     "human",
                     "{question}"
                )
            ]
        )
        tracer = LangChainTracer() #trace the llm call to langsmith
        chain = prompt | self.llm
        stand_alone_q = chain.invoke(
            {
                "chat_history": chat_history_summary, 
                "question": question
            },
            config={"callbacks": [tracer]}).content
        return Question(stand_alone_q)