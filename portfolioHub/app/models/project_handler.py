from typing import List, Any, Dict
from pymongo.collection import Collection
from .db_handler import DbHandler
from .project import Project
from .badge import Badge
from ..utils.type import Type
from datetime import datetime

class ProjectHandler(DbHandler):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, projects: List[Project]) -> Dict[str, int]:
        if not all(isinstance(project, Project) for project in projects):
            raise ValueError("Input data expected to be a list of Project")
        
        projects_data = []
        for project in projects:
            data = {
                'type': Type.PROJECT.value,
                'createdAt': datetime.today()
            }
            data.update(project.model_dump(by_alias=True))
            projects_data.append(data)

        result = self.collection.insert_many(projects_data).inserted_ids
        return result
    
    def find(self, filter: Dict[str,Any], max: int = 5, skip: int = 0) -> List[Project]:
        cursor = self.collection.find(filter).skip(skip).limit(max)
        projects = []

        for doc in cursor:
            project = Project(
                user_id = doc["userId"],
                name = doc["name"],
                description = doc["description"],
                badges = [Badge(**badge) for badge in doc["badges"]],
                images = doc["images"],
                url = doc["url"]
            )
            projects.append(project)

        if len(projects) > 0:
            return projects
        return None
    
    def delete(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}