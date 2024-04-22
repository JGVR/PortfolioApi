from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .person import Person

class PersonCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, person: Person) -> bool:
        person_data = person.model_dump(by_alias=True)
        return self.collection.insert_one(person_data).acknowledged
    
    def insert_many(self, persons: List[Person]) -> bool:
        persons_data = [person.model_dump(by_alias=True) for person in persons]
        return self.collection.insert_many(persons_data).acknowledged
    
    def find_one(self, filter: Dict[str,Any]) -> Person:
        data = self.collection.find_one(filter)
        return Person(**data)
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Person]:
        cursor = self.collection.find(filter).limit(max_docs)
        persons = [Person(**document) for document in cursor]
        return persons
    
    def delete_one(self, filter: Dict[str,Any]) -> bool:
        return self.collection.delete_one(filter).acknowledged
    
    def delete_many(self, filter: Dict[str,Any]) -> bool:
        return self.collection.delete_many(filter).acknowledged
    
    def upsert_one(self, filter: Person | Dict[str,Any], modifications: Person | Dict[str,Any]) -> bool:
        person_data = filter.model_dump(by_alias=True) if isinstance(filter, Person) else filter
        changes = modifications.model_dump(by_alias=True) if isinstance(modifications, Person) else modifications
        return self.collection.update_one(person_data, {"$set": changes}, upsert=True).acknowledged
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)
    