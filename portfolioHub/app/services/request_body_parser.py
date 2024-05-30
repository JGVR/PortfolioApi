from .model_identifier import ModelIdentifier
from .embedding_generator import EmbeddingGenerator
from langchain_openai import OpenAIEmbeddings
from ..models.person import Person
from ..models.achievement import Achievement
from ..models.experience import Experience
from ..models.project import Project
from ..config import config
from typing import Dict, Any, Union, List

class RequestBodyParser:
    @staticmethod
    def parse_request_body(request_body: Dict[str,Any]) -> Union[Person, Achievement, Project, Experience] | List[Union[Person, Achievement, Project, Experience]]:
        collection_name = request_body["collection"]
        request_body.pop("collection")
        llm = OpenAIEmbeddings(model=config.openai_embedding_model, openai_api_key=config.openai_api_key)

        #check if the request body has more than 1 record
        if isinstance(request_body["data"], list):
            for i in range(len(request_body["data"])):
                #generate embeddings for each record
                embeddings = EmbeddingGenerator(llm).call(request_body["data"][i])
                request_body["data"][i].update({"embeddings": embeddings})
            results = [ModelIdentifier.identify_model(collection_name, model_data) for model_data in request_body["data"]]
            return results
        
        #if there is only 1 record in the request_body then generate embeddings for that record
        embeddings = EmbeddingGenerator(llm=llm).call(request_body["data"])
        request_body["data"]["embeddings"] = embeddings
        return ModelIdentifier.identify_model(collection_name, request_body["data"])