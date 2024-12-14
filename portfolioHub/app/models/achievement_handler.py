from typing import List, Any, Dict
from pymongo.collection import Collection
from .db_handler import DbHandler
from .achievement import Achievement
from .certificate import Certificate
from .degree import Degree
from .edu_entity import EduEntity
from ..utils.type import Type
from ..utils.achiev_type import AchievType
from datetime import datetime
from bson import ObjectId

class AchievementHandler(DbHandler):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, achiev: Achievement) -> Dict[str, int]:
        if not isinstance(achiev, Achievement):
            raise ValueError("Input data expected to be an Achievement object")
        
        achievements_data = []
        #Identify the type of achievemnt, and create dict based on the achiev schema
        if len(achiev.certificates) >= 1:
            for cert in achiev.certificates:
                data = {
                    '_id': ObjectId(),
                    'type': Type.ACHIEVEMENT.value,
                    'createdAt': datetime.today(),
                    'userId': achiev.user_id,
                    'achievType': AchievType.CERTIFICATE.value,
                    'name': cert.name,
                    'description': cert.description,
                    'url': cert.url,
                    'eduEntity': cert.platform.name
                }
                achievements_data.append(data)
        
        if len(achiev.degrees) >= 1:
            for degree in achiev.degrees:
                data = {
                    '_id': ObjectId(),
                    'type': Type.ACHIEVEMENT.value,
                    'createdAt': datetime.today(),
                    'userId': achiev.user_id,
                    'achievType': AchievType.DEGREE.value,
                    'name': degree.name,
                    'description': degree.description,
                    'url': degree.url,
                    'eduEntity': degree.school.name
                }
                achievements_data.append(data)

        result = self.collection.insert_many(achievements_data).inserted_ids
        return result
    
    def find(self, filter: Dict[str,Any], max_docs: int = 5) -> Achievement:
        cursor = self.collection.find(filter).limit(max_docs)
        certs = []
        degrees = []
        user_id = None

        for doc in cursor:
            #Create Certificate
            if doc["achievType"] == "certificates":
                cert = Certificate(
                    name = doc["name"],
                    description = doc["description"],
                    url = doc["url"],
                    platform = EduEntity(name=doc["eduEntity"])
                )
                certs.append(cert)
            
            #Create Degree
            if doc["achievType"] == "degree":
                degree = Degree(
                    name = doc["name"],
                    description = doc["description"],
                    url = doc["url"],
                    school = EduEntity(name=doc["eduEntity"])
                )
                degrees.append(degree)
            user_id = doc["userId"]
        
        #Create achievement
        achiev = Achievement(
            user_id = user_id,
            certificates = certs,
            degrees = degrees
        )

        if achiev is not None :
            return achiev
        return None
    
    def delete(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}