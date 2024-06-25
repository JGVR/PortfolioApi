from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .person import Person

class PersonCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, person: Person) -> Dict[str, int]:
        if not isinstance(person, Person):
            raise ValueError("Input data expected to be a Person object")
        person_data = person.model_dump(by_alias=True)
        return {"_id":self.collection.insert_one(person_data).inserted_id}
    
    def insert_many(self, persons: List[Person]) -> List[Dict[str,int]]:
        if not all(isinstance(person, Person) for person in persons):
            raise ValueError("Input data expected to be a list of Person")
        persons_data = [person.model_dump(by_alias=True) for person in persons]
        result = [{"_id": id} for id in self.collection.insert_many(persons_data).inserted_ids]
        return result
    
    def find_one(self, filter: Dict[str,Any]) -> Person:
        data = self.collection.find_one(filter)
        print(data)
        if data is not None:
            return Person(**data)
        return None
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Person]:
        cursor = self.collection.find(filter).limit(max_docs)
        persons = [Person(**document) for document in cursor]

        if len(persons) > 0:
            return persons
        return None

    def delete_one(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_one(filter).deleted_count}
    
    def delete_many(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Person | Dict[str,Any]) -> Dict[str,int]:
        person_data = modifications.model_dump(by_alias=True) if isinstance(modifications, Person) else modifications
        upsert_result = self.collection.update_one(filter, {"$set": person_data}, upsert=True)
        result = {"count":upsert_result.modified_count} if upsert_result.modified_count > 0 else {"_id":upsert_result.upserted_id}
        return result
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)
    