from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .person import Person

class PersonCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, person: Person) -> int:
        if not isinstance(person, Person):
            raise ValueError("Input data expected to be a Person object")
        person_data = person.model_dump(by_alias=True)
        return self.collection.insert_one(person_data).inserted_id
    
    def insert_many(self, persons: List[Person]) -> List[int]:
        if not all(isinstance(person, Person) for person in persons):
            raise ValueError("Input data expected to be a list of Person")
        persons_data = [person.model_dump(by_alias=True) for person in persons]
        return self.collection.insert_many(persons_data).inserted_ids
    
    def find_one(self, filter: Dict[str,Any]) -> Person:
        data = self.collection.find_one(filter)
        if data is not None:
            return Person(**data)
        return None
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Person]:
        cursor = self.collection.find(filter).limit(max_docs)
        persons = [Person(**document) for document in cursor]

        if len(persons) > 0:
            return persons
        return None

    def delete_one(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_one(filter).deleted_count
    
    def delete_many(self, filter: Dict[str,Any]) -> int:
        return self.collection.delete_many(filter).deleted_count
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Person | Dict[str,Any]) -> int:
        person_data = filter
        changes = modifications.model_dump(by_alias=True) if isinstance(modifications, Person) else modifications
        result = self.collection.update_one(person_data, {"$set": changes}, upsert=True)
        return result.modified_count if result.modified_count > 0 else result.upserted_id
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)
    