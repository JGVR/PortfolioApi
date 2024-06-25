from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .experience import Experience

class ExperienceCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, experience: Experience) -> Dict[str,int]:
        if not isinstance(experience, Experience):
            raise ValueError("Input data expected to be a Experience object")
        experience_data = experience.model_dump(by_alias=True)
        return {"_id":self.collection.insert_one(experience_data).inserted_id}
    
    def insert_many(self, experiences: List[Experience]) -> List[Dict[str,int]]:
        if not all(isinstance(experience, Experience) for experience in experiences):
            raise ValueError("Input data expected to be a list of Experience")
        experiences_data = [experience.model_dump(by_alias=True) for experience in experiences]
        result = [{"_id": id} for id in self.collection.insert_many(experiences_data).inserted_ids]
        return result
    
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

    def delete_one(self, filter: Dict[str,Any]) -> Dict[str, int]:
        return {"count":self.collection.delete_one(filter).deleted_count}
    
    def delete_many(self, filter: Dict[str,Any]) -> Dict[str, int]:
        return {"count":self.collection.delete_many(filter).deleted_count}
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Experience | Dict[str,Any]) -> Dict[str,int]:
        experience_data = modifications.model_dump(by_alias=True) if isinstance(modifications, Experience) else modifications
        upsert_result = self.collection.update_one(filter, {"$set": experience_data}, upsert=True)
        result = {"count":upsert_result.modified_count} if upsert_result.modified_count > 0 else {"_id":upsert_result.upserted_id}
        return result
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)