from ..models.person import Person
from ..models.achievement import Achievement
from ..models.experience import Experience
from ..models.project import Project
from typing import Dict, Any, Union

class ModelIdentifier:
    @staticmethod
    def identify_model(collection_name: str, data: Dict[str, Any]) -> Union[Person, Achievement, Project, Experience]:
        if 'persons' in collection_name:
            return Person(**data)
        elif 'projects' in collection_name:
            return Project(**data)
        elif 'experience' in collection_name:
            return Experience(**data)
        else:
            return Achievement(**data)