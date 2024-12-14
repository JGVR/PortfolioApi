from .model_identifier import ModelIdentifier
from ..models.profile import Profile
from ..models.achievement import Achievement
from ..models.experience import Experience
from ..models.project import Project
from ..models.user import User
from typing import Dict, Any, Union, List

class RequestBodyParser:
    @staticmethod
    def parse_request_body(request_body: Dict[str,Any]) -> Union[User, Profile, Achievement, Project, Experience] | List[Union[User, Profile, Achievement, Project, Experience]]:
        model_type = request_body["type"]

        #check if the request body has more than 1 record
        if isinstance(request_body["data"], list):
            results = [ModelIdentifier.identify_model(model_type, model_data) for model_data in request_body["data"]]
            return results
        return ModelIdentifier.identify_model(model_type, request_body["data"])