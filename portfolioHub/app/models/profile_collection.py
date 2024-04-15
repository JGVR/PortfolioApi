from typing import List, Any, Dict
from pymongo.collection import Collection
from dbcollection import DbCollection
from person import Person
from pymongo import MongoClient

class ProfileCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, person: Person) -> bool:
        return True
    
    def insert_many(self, persons: List[Person]) -> bool:
        return True
    
    def find_one(self, filter: Dict[str,Any]) -> Person:
        data = self.collection.find_one(filter)
        return Person(**data)
    
    def find_many(self, filter: Dict[str,Any], max_docs: int = 5) -> List[Person]:
        cursor = self.collection.find(filter).limit(max_docs)
        persons = []
        for document in cursor:
            persons.append(Person(**document))
        return persons
    
    def delete_one(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def delete_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def upsert_one(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def upsert_many(self, filter: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)
    

cluster = MongoClient("mongodb+srv://jv_admin:Th0r3s3lDi0sDelTrueno1130!@portfolio.jmd2tdg.mongodb.net/?retryWrites=true&w=majority&appName=Portfolio")
db = cluster["portfolio"]
collection = ProfileCollection(db["profiles"])
count = collection.count({
    "_id": 1
})
filter = {
    "_id": 1,
    "firstName": "Juan"
}
docs = collection.find_many(max_docs=1)
print(docs)