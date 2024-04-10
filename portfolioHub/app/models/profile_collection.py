from typing import List, Any, Dict
from pymongo.collection import Collection
from dbcollection import DbCollection
from person import Person

class ProfileCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, person: Person) -> bool:
        return True
    
    def insert_many(self, persons: List[Person]) -> bool:
        return True
    
    def find_one(self, filters: Dict[str,Any]) -> Person:
        #needs to be adjusted so that a Person is returned
        return self.collection.find_one(filters)
    
    def find_many(self, filters: Dict[str,Any]) -> List[Person]:
        return True
    
    def delete_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def delete_many(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_one(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def upsert_many(self, filters: Dict[str,Any]) -> bool:
        return True