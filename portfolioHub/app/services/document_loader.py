from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from dataclasses import dataclass
from typing import List
from ..config import config
from pymongo import MongoClient

@dataclass(frozen=True)
class AtlasDocumentLoader:
    embedding_model: OpenAIEmbeddings
    collection_name: str
    embedding_key: str
    index_name: str

    def call(self, docs: List[Document]):
        cluster = MongoClient(config.atlas_conn_str)
        db = cluster[config.atlas_db_name]
        collection = db[self.collection_name]
        MongoDBAtlasVectorSearch.from_documents(documents=docs, embedding=self.embedding_model, collection=collection, embedding_key=self.embedding_key, index_name=self.index_name)


