from dataclasses import dataclass
from typing import Dict, Any, List
from langchain_openai import OpenAIEmbeddings
import json

@dataclass(frozen=True)
class EmbeddingGenerator:
    llm: OpenAIEmbeddings

    def call(self, data: Dict[str, Any]) -> List[float]:
        json_data = json.dumps(data)
        embeddings = self.llm.embed_query(json_data)
        return embeddings