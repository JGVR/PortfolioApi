from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict, Any
import json

class DocumentGenerator:
    @staticmethod
    def call(request_data: Dict[str, Any] | List[Dict[str,Any]]) -> List[Document]:
        data = []
        if isinstance(request_data, list):
            for doc in request_data:
                data.append(Document(page_content=json.dumps(doc), metadata={
                    "id": doc["_id"],
                    "achievement_ids": doc.get("achievement_ids", None),
                    "project_ids": doc.get("project_ids", None),
                    "experience_ids": doc.get("experience_ids", None),
                    "personId": doc.get("personId", None)
                }))
        else:
            data.append(Document(page_content=json.dumps(request_data), metadata={
                "id": request_data["_id"],
                "achievement_ids": request_data.get("achievement_ids", None),
                "project_ids": request_data.get("project_ids", None),
                "experience_ids": request_data.get("experience_ids", None),
                "personId": request_data.get("personId", None)
            }))
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        docs = text_splitter.split_documents(data)
        return docs