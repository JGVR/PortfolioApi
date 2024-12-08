from ..models.user_handler import UserHandler
from ..models.achievement_handler import AchievementHandler
from ..models.experience_handler import ExperienceHandler
from ..models.profile_handler import ProfileHandler
from ..models.project_handler import ProjectHandler
from pymongo.collection import Collection

class HandlerIdentifier:
    @staticmethod
    def call(collection: Collection, type: str):
        match type:
            case "user":
                return UserHandler(collection)
            case "project":
                return ProjectHandler(collection)
            case "profile":
                return ProfileHandler(collection)
            case "experience":
                return ExperienceHandler(collection)
            case _:
                return AchievementHandler(collection)