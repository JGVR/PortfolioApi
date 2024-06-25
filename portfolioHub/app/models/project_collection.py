from typing import List, Any, Dict
from pymongo.collection import Collection
from .dbcollection import DbCollection
from .project import Project

class ProjectCollection(DbCollection):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_one(self, project: Project) -> Dict[str,int]:
        if not isinstance(project, Project):
            raise ValueError("Input data expected to be a Project object")
        project_data = project.model_dump(by_alias=True)
        return {"_id":self.collection.insert_one(project_data).inserted_id}
    
    def insert_many(self, projects: List[Project]) -> List[Dict[str,int]]:
        if not all(isinstance(project, Project) for project in projects):
            raise ValueError("Input data expected to be a Project object")
        projects_data = [project.model_dump(by_alias=True) for project in projects]
        result = [{"_id":id} for id in self.collection.insert_many(projects_data).inserted_ids]
        return result
    
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
    
    def delete_one(self, filters: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_one(filters).deleted_count}
    
    def delete_many(self, filters: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filters).deleted_count}
    
    def upsert_one(self, filter: Dict[str,Any], modifications: Project | Dict[str,Any]) -> Dict[str,int]:
        project_data = modifications.model_dump(by_alias=True) if isinstance(modifications, Project) else modifications
        upsert_result = self.collection.update_one(filter, {"$set": project_data}, upsert=True)
        result = {"_id":upsert_result.modified_count} if upsert_result.modified_count > 0 else {"_id":upsert_result.upserted_id}
        return result

    def upsert_many(self, filters: Dict[str,Any]) -> bool:
        return True
    
    def count(self, filter: Dict[str,Any]) -> int:
        return self.collection.count_documents(filter)