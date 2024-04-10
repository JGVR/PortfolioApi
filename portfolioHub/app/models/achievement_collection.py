from typing import List, Any, Dict
from pymongo.collection import Collection
from dbcollection import DbCollection
from achievement import Achievement

class AchievementCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, achievement: Achievement) -> bool:
        return True
    
    def insert_many(self, achievements: List[Achievement]) -> bool:
        return True
    
    def find_one(self, filters: Dict[str,Any]) -> Achievement:
        #needs to be adjusted so that an Achievement is returned
        return self.collection.find_one(filters)
    
    def find_many(self, filters: Dict[str,Any]) -> List[Achievement]:
        return True
    
    def delete_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def delete_many(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_many(self, filters: Dict[str,Any]) -> bool:
        return True