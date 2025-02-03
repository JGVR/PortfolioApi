from typing import Dict, Any
from ..models.achievement import Achievement
from ..models.profile import Profile
from ..models.experience import Experience
from ..models.project import Project
from ..models.user import User

class ResponseParser:
    @staticmethod
    def parse_response(data) -> Dict[str, Any]:
        print(data)
        if data is None:
            return {"result": "None"}
        else:
            if isinstance(data, list):
                if isinstance(data[0], dict):
                    return data
                else:
                    return [entity.model_dump(by_alias=True) for entity in data]
            elif isinstance(data, dict):
                return data
            else:
                return data.model_dump(by_alias=True)