from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from channels.generic.websocket import WebsocketConsumer
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from ..services.chat_history_summarizer import ChatHistorySummarizer
from ..services.doc_retriever import DocRetriever
from ..services.chatbot import ChatBot
from ..services.follow_up_question_builder import FollowUpQuestionBuilder
from ..utils.question import Question
from ..utils.answer import Answer
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
            llm = ChatOpenAI(model="gpt-4o", api_key=config.openai_api_key, temperature=0.5)
            question = Question(data["question"])
            stand_alone_q = FollowUpQuestionBuilder(llm).call(question, self.chat_history)
            cluster = MongoClient(config.atlas_conn_str)
            db = cluster[config.atlas_db_name]
            mongo_db = MongoDBAtlasVectorSearch(db[config.atlas_vector_collection], embedding=OpenAIEmbeddings(model=config.openai_embedding_model, api_key=config.openai_api_key), index_name=config.atlas_vector_idx_name, embedding_key=config.atlas_embedding_key)
            relevant_docs = DocRetriever(mongo_db, 3).call(stand_alone_q)
            chat_history_summary = ChatHistorySummarizer(llm=llm).call(self.chat_history)
            chatbot = ChatBot(llm=llm)
            chunks = []
            
            #stream chatbot responses
            for chunk in chatbot.call(stand_alone_q.text, chat_history_summary, relevant_docs):
                chunks.append(chunk)
                response = {
                    "event": "qa",
                    "question": stand_alone_q.text,
                    "text": chunk
                }
                self.send(text_data=json.dumps(response))

            #send full answer
            answer = Answer.from_chunks(chunks, stand_alone_q)
            response = {
                "event": "answer",
                "message": answer.serialize()
            }
            self.send(text_data=json.dumps(response))

            #add messages to chat history
            self.chat_history.add_user_message(question.text)
            self.chat_history.add_ai_message(stand_alone_q.text)
        else:
            response = {
                "event": "error",
                "text": f"""The following event is not available: {data["event"]}"""
            }
            self.send(text_data=json.dumps(response))
    def disconnect(self, close_code):
        pass