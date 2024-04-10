from typing import List, Any, Dict
from pymongo.collection import Collection
from dbcollection import DbCollection
from project import Project

class ProjectCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, project: Project) -> bool:
        return True
    
    def insert_many(self, persons: List[Project]) -> bool:
        return True
    
    def find_one(self, filters: Dict[str,Any]) -> Project:
        #needs to be adjusted so that a Project is returned
        return self.collection.find_one(filters)
    
    def find_many(self, filters: Dict[str,Any]) -> List[Project]:
        return True
    
    def delete_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def delete_many(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_many(self, filters: Dict[str,Any]) -> bool:
        return True