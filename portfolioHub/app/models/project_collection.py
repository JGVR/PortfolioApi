from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .project import Project

class ProjectCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, project: Project) -> int:
        if not isinstance(project, Project):
            raise ValueError("Input data expected to be a Project object")
        project_data = project.model_dump(by_alias=True)
        return self.collection.insert_one(project_data).inserted_id
    
    def insert_many(self, projects: List[Project]) -> List[int]:
        if not all(isinstance(project, Project) for project in projects):
            raise ValueError("Input data expected to be a Project object")
        projects_data = [project.model_dump(by_alias=True) for project in projects]
        return self.collection.insert_many(projects_data).inserted_ids
    
    def find_one(self, filters: Dict[str,Any]) -> Project:
        project = self.collection.find_one(filters)
        if project is not None:
            return Project(**project)
        return None
    
    def find_many(self, filters: Dict[str,Any], max_docs: int = 5) -> List[Project]:
        cursor = self.collection.find(filters).limit(max_docs)
        projects = [Project(**data) for data in cursor]

        if len(projects) > 0:
            return projects
        return None
    
    def delete_one(self, filters: Dict[str,Any]) -> int:
        return self.collection.delete_one(filters).deleted_count
    
    def delete_many(self, filters: Dict[str,Any]) -> int:
        return self.collection.delete_many(filters).deleted_count
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Project | Dict[str,Any]) -> int:
        changes = modifications.model_dump(by_alias=True) if isinstance(modifications, Project) else modifications
        result = self.collection.update_one(filter, {"$set": changes}, upsert=True)
        return result.modified_count if result.modified_count > 0 else result.upserted_id

    def upsert_many(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)