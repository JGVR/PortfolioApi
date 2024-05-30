from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .experience import Experience

class ExperienceCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, experience: Experience) -> int:
        if not isinstance(experience, Experience):
            raise ValueError("Input data expected to be a Experience object")
        experience_data = experience.model_dump(by_alias=True)
        return self.collection.insert_one(experience_data).inserted_id
    
    def insert_many(self, experiences: List[Experience]) -> List[int]:
        if not all(isinstance(experience, Experience) for experience in experiences):
            raise ValueError("Input data expected to be a list of Experience")
        experiences_data = [experience.model_dump(by_alias=True) for experience in experiences]
        return self.collection.insert_many(experiences_data).inserted_ids
    
    def find_one(self, filter: Dict[str,Any]) -> Experience:
        data = self.collection.find_one(filter)
        if data is not None:
            return Experience(**data)
        return None
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Experience]:
        cursor = self.collection.find(filter).limit(max_docs)
        experiences = [Experience(**document) for document in cursor]

        if len(experiences) > 0:
            return experiences
        return None

    def delete_one(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_one(filter).deleted_count
    
    def delete_many(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_many(filter).deleted_count
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Experience | Dict[str,Any]) -> int:
        changes = modifications.model_dump(by_alias=True) if isinstance(modifications, Experience) else modifications
        result = self.collection.update_one(filter, {"$set": changes}, upsert=True)
        return result.modified_count if result.modified_count > 0 else result.upserted_id
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)