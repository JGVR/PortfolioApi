from langchain_mongodb import MongoDBAtlasVectorSearch
from ..utils.question import Question
from ..utils.relevant_doc import RelevantDoc
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DocRetriever:
    vector_store: MongoDBAtlasVectorSearch
    k: int

    def call(self, question: Question) -> List[RelevantDoc]:
        docs = self.vector_store.similarity_search(question.text, self.k)
        return [RelevantDoc(content=doc.page_content) for doc in docs]