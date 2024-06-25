from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .achievement import Achievement

class AchievementCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, achievement: Achievement) -> Dict[str,int]:
        if not isinstance(achievement, Achievement):
            raise ValueError("Input data expected to be a Achievement object")
        achievement_data = achievement.model_dump(by_alias=True)
        return {"_id":self.collection.insert_one(achievement_data).inserted_id}
    
    def insert_many(self, achievements: List[Achievement]) -> List[Dict[str,int]]:
        if not all(isinstance(achievement, Achievement) for achievement in achievements):
            raise ValueError("Input data expected to be a list of Achievement")
        achievements_data = [achievement.model_dump(by_alias=True) for achievement in achievements]
        results = [{"_id": id} for id in self.collection.insert_many(achievements_data).inserted_ids]
        return results
    
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

    def delete_one(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_one(filter).deleted_count}
    
    def delete_many(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Achievement | Dict[str,Any]) -> Dict[str,int]:
        achievement_data = modifications.model_dump(by_alias=True) if isinstance(modifications, Achievement) else modifications
        upsert_result = self.collection.update_one(filter, {"$set": achievement_data}, upsert=True)
        result = {"count": upsert_result.modified_count} if upsert_result.modified_count > 0 else {"_id":upsert_result.upserted_id}
        return result
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)