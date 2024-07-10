from typing import List, Any, Dict
from pymongo.collection import Collection
from .db_handler import DbHandler
from .user import User
from ..utils.type import Type
from datetime import datetime

class UserHandler(DbHandler):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, users: List[User]) -> Dict[str, int]:
        if not all(isinstance(user, User) for user in users):
            raise ValueError("Input data expected to be a list of User")
        
        users_data = []
        for user in users:
            data = {
                'type': Type.USER.value,
                'createdAt': datetime.today
            }
            data.update(user.model_dump(by_alias=True))
            users_data.append(data)

        result = [{"_id": id} for id in self.collection.insert_many(users_data).inserted_ids]
        return result
    
    def find(self, filter: Dict[str,Any], max_docs: int = 5) -> List[User]:
        cursor = self.collection.find(filter).limit(max_docs)
        users = []

        for doc in cursor:
            user = User(
                userId = doc["userId"],
                emailAddress = doc["emailAddress"]
            )
            users.append(user)

        if len(users) > 0:
            return users
        return None
    
    def delete_many(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}