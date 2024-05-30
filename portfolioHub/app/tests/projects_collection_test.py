import pytest
from datetime import datetime
from portfolioHub.app.models.project_collection import ProjectCollection
from portfolioHub.app.models.project import Project
from portfolioHub.app.models.skill import Skill
from pymongo import MongoClient
from config import config
from pydantic import ValidationError as PValidationError


class TestProjectCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolio"]
    collection = ProjectCollection(db["projects"])
    
    def test_insert_one_project(self):
        project1 = Project(
            _id = 1,
            personId = 1,
            name = "Gaius Chatbot",
            description = "This was a chatbot that answered any legal questions using only legal sentences stored in Azure Blob Services",
            skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone")],
        )
        result = self.collection.insert_one(project1)
        assert result == 1
    
    def test_insert_one_project_with_an_non_existing_person_id(self):
        with pytest.raises(ValueError) as exc_info:
            project1 = Project(
            _id = 2,
            personId = 15,
            name = "Project Portfolio",
            description = "This was a project that I build to showcase my skills and experience.",
            skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone"), Skill(name="MongoDB")],
        )
        assert f"The person Id: 15 was not found in the persons collections. Please make sure the person exists before assigning a project to a person." in str(exc_info.value)

    def test_insert_one_already_in_db(self):
        project1 = Project(
            _id = 1,
            personId = 1,
            name = "Gaius Chatbot",
            description = "This was a chatbot that answered any legal questions using only legal sentences stored in Azure Blob Services",
            skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone")],
        )
        with pytest.raises(Exception) as exc:
            self.collection.insert_one(project1)
        assert "duplicate key error" in str(exc.value)
    
    def test_insert_one_with_a_non_project_arg(self):
        with pytest.raises(ValueError) as ex:
            self.collection.insert_one({"_id":7})
        assert "Input data expected to be a Project object" in str(ex.value)

    def test_insert_many_complete_projects(self):
        projects = [
            Project(
                _id = 2,
                personId = 1,
                name = "Portfolio Prpject",
                description = "This was a project to showcase my ability and skills",
                skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone"), Skill(name="MongoDB")]
            ),
            Project(
                _id = 3,
                personId = 1,
                name = "SSIS Projects",
                description = "Multiple projects done with ssis",
            )
        ]
        result = self.collection.insert_many(projects)
        assert result[0] == 2
        assert result[1] == 3

    def test_insert_many_already_in_db(self):
        projects = [
           Project(
                _id = 2,
                personId = 1,
                name = "Portfolio Prpject",
                description = "This was a project to showcase my ability and skills",
                skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone"), Skill(name="MongoDB")]
            ),
            Project(
                _id = 3,
                personId = 1,
                name = "SSIS Projects",
                description = "Multiple projects done with ssis",
            )
       ]
        with pytest.raises(Exception) as exc:
            self.collection.insert_many(projects)
        assert "duplicate key error" in str(exc.value)

    def test_find_one_returns_correct_project(self):
        project = self.collection.find_one({"_id":1})
        assert project.model_dump(by_alias=True)["_id"] == 1

    def test_find_one_project_not_in_db(self):
        project = self.collection.find_one({"_id": 15})
        assert project == None

    def test_find_many_returns_correct_projects(self):
        projects = self.collection.find_many({"personId": 1})
        assert all(project.person_id for project in projects)

    def test_find_many_projects_not_in_db(self):
        projects = self.collection.find_many({"_id": 5})
        assert projects == None
    
    def test_find_many_returns_correct_amt_of_projects(self):
        projects = self.collection.find_many({"personId": 1}, 2)
        assert len(projects) == 2

    def test_delete_one_project(self):
        result = self.collection.delete_one({"_id":3})
        assert result == 1
    
    def test_delete_one_project_not_in_db(self):
        result = self.collection.delete_one({"_id": 15})
        assert result == 0

    def test_delete_many_project(self):
        result = self.collection.delete_many({"personId": 1})
        assert result == 2
    
    def test_delete_many_project_not_in_db(self):
        result = self.collection.delete_many({"skills": {"name": "C#"}})
        assert result == 0

    def test_upsert_one_existing_project(self):
        project1 = Project(
            _id = 1,
            personId = 1,
            name = "Gaius Chatbot",
            description = "This was a chatbot that answered any legal questions using only legal sentences stored in Azure Blob Services",
            skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone"), Skill(name="Pydantic")],
        )
        filter = {"_id": 1}
        result = self.collection.upsert_one(filter, project1)
        assert result == 1

    def test_upsert_one_new_project(self):
        project1 = Project(
            _id = 4,
            personId = 1,
            name = "Gaius Chatbot",
            description = "This was a chatbot that answered any legal questions using only legal sentences stored in Azure Blob Services",
            skills = [Skill(name="python"), Skill(name="Langchain"), Skill(name="Pinecone")],
        )
        filter = {"_id": 4}
        result = self.collection.upsert_one(filter, project1)
        assert result == 4