from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .achievement import Achievement

class AchievementCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, achievement: Achievement) -> int:
        if not isinstance(achievement, Achievement):
            raise ValueError("Input data expected to be a Achievement object")
        achievement_data = achievement.model_dump(by_alias=True)
        return self.collection.insert_one(achievement_data).inserted_id
    
    def insert_many(self, achievements: List[Achievement]) -> List[int]:
        if not all(isinstance(achievement, Achievement) for achievement in achievements):
            raise ValueError("Input data expected to be a list of Achievement")
        achievements_data = [achievement.model_dump(by_alias=True) for achievement in achievements]
        return self.collection.insert_many(achievements_data).inserted_ids
    
    def find_one(self, filter: Dict[str,Any]) -> Achievement:
        data = self.collection.find_one(filter)
        if data is not None:
            return Achievement(**data)
        return None
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Achievement]:
        cursor = self.collection.find(filter).limit(max_docs)
        achievements = [Achievement(**document) for document in cursor]

        if len(achievements) > 0:
            return achievements
        return None

    def delete_one(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_one(filter).deleted_count
    
    def delete_many(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_many(filter).deleted_count
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Achievement | Dict[str,Any]) -> int:
        changes = modifications.model_dump(by_alias=True) if isinstance(modifications, Achievement) else modifications
        result = self.collection.update_one(filter, {"$set": changes}, upsert=True)
        return result.modified_count if result.modified_count > 0 else result.upserted_id
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)