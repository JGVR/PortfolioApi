from ..models.person_collection import PersonCollection
from ..models.achievement_collection import AchievementCollection
from ..models.experience_collection import ExperienceCollection
from ..models.project_collection import ProjectCollection
from pymongo import MongoClient
from ..config import config

class CollectionIdentifier:
    @staticmethod
    def identify_collection(collection_name: str):
        cluster = MongoClient(config.atlas_conn_str)
        db = cluster[config.atlas_db_name]

        if 'persons' in collection_name:
            return PersonCollection(db[collection_name])
        elif 'projects' in collection_name:
            return ProjectCollection(db[collection_name])
        elif 'experience' in collection_name:
            return ExperienceCollection(db[collection_name])
        else:
            return AchievementCollection(db[collection_name])