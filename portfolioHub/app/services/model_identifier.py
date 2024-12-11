from ..models.achievement import Achievement
from ..models.experience import Experience
from ..models.project import Project
from ..models.user import User
from ..models.profile import Profile
from typing import Dict, Any, Union

class ModelIdentifier:
    @staticmethod
    def identify_model(model_type: str, data: Dict[str, Any]) -> Union[User, Profile, Achievement, Project, Experience]:
        match model_type:
            case "user":
                return User(**data)
            case "profile":
                return Profile(
                    userId=data["userId"],
                    firstName=data["firstName"],
                    lastName=data["lastName"],
                    dateOfBirth=data["dateOfBirth"],
                    hobbies=data["hobby"],
                    skills=data["skills"],
                    shortBio = data["shortBio"],
                    bio=data["bio"],
                    countryOfBirth=data["countryOfBirth"],
                    countryOfResidence=data["countryOfResidence"],
                    linkedInUrl=data["linkedInUrl"],
                    gitHubUrl=data["gitHubUrl"]
                )
            case "project":
                return Project(**data)
            case "experience":
                return Experience(**data)
            case "achievement":
                return Achievement(**data)
            case _:
                raise ValueError(f"Invalid type {model_type}")