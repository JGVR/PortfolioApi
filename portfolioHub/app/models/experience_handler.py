from typing import List, Any, Dict
from pymongo.collection import Collection
from .db_handler import DbHandler
from .experience import Experience
from .company import Company
from ..utils.type import Type
from datetime import datetime
from bson import ObjectId

class ExperienceHandler(DbHandler):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, exps: List[Experience]) -> List[ObjectId]:
        if not all(isinstance(exp, Experience) for exp in exps):
            raise ValueError("Input data expected to be a list of Experience")
        
        exps_data = []
        for exp in exps:
            data = {
                '_id': ObjectId(),
                'type': Type.EXPERIENCE.value,
                'createdAt': datetime.today(),
                'userId': exp.user_id,
                'jobTitle': exp.job_title,
                'jobDescription': exp.job_description,
                'company': exp.company.name,
                'startDate': exp.start_date,
                'endDate': exp.end_date
            }
            exps_data.append(data)

        result = self.collection.insert_many(exps_data).inserted_ids
        return result
    
    def find(self, filter: Dict[str,Any], max: int = 5, skip: int = 0) -> List[Experience]:
        cursor = self.collection.find(filter).skip(skip).limit(max)
        exps = []

        for doc in cursor:
            exp = Experience(
                user_id = doc["userId"],
                job_title = doc["jobTitle"],
                job_description = doc["jobDescription"],
                company = Company(name=doc["company"]),
                start_date = doc["startDate"],
                end_date = doc["endDate"]
            )
            exps.append(exp)

        if len(exps) > 0:
            return exps
        return None
    
    def delete(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}