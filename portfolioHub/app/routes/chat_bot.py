from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from channels.generic.websocket import WebsocketConsumer
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from ..services.chat_history_summarizer import ChatHistorySummarizer
from ..services.doc_retriever import DocRetriever
from ..services.follow_up_question_builder import FollowUpQuestionBuilder
from ..utils.question import Question
from ..config import config
from pymongo import MongoClient
import json

class ChatBotConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.chat_history = ChatMessageHistory()
        msg = {"message": "Connection Successful!"}
        self.send(text_data=json.dumps(msg))

    def receive(self, text_data):
        data = json.loads(text_data)
        if data["event"] == "qa":
            llm = ChatOpenAI(model=config.openai_chat_model, api_key=config.openai_api_key, temperature=0.5)
            question = Question(data["question"])
            stand_alone_q = FollowUpQuestionBuilder(llm).call(question, self.chat_history)
            cluster = MongoClient(config.atlas_conn_str)
            db = cluster[config.atlas_db_name]
            mongo_db = MongoDBAtlasVectorSearch(db[config.atlas_vector_collection], embedding=OpenAIEmbeddings(model=config.openai_embedding_model, api_key=config.openai_api_key), index_name=config.atlas_vector_idx_name, embedding_key=config.atlas_embedding_key)
            relevant_docs = DocRetriever(mongo_db, 3).call(stand_alone_q)
            response = {
                "event": "qa",
                "question": stand_alone_q.text,
                "docs": [doc.content for doc in relevant_docs]
            }
            self.send(text_data=json.dumps(response))

    def disconnect(self, close_code):
        pass