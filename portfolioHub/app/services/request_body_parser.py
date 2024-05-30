from .model_identifier import ModelIdentifier
from ..models.person import Person
from ..models.achievement import Achievement
from ..models.experience import Experience
from ..models.project import Project
from typing import Dict, Any, Union, List

class RequestBodyParser:
    @staticmethod
    def parse_request_body(request_body: Dict[str,Any]) -> Union[Person, Achievement, Project, Experience] | List[Union[Person, Achievement, Project, Experience]]:
        collection_name = request_body["collection"]
        request_body.pop("collection")
        if isinstance(request_body["data"], list):
            results = [ModelIdentifier.identify_model(collection_name, model_data) for model_data in request_body["data"]]
            return results
        return ModelIdentifier.identify_model(collection_name, request_body["data"])