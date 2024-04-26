import pytest
from datetime import datetime
from portfolioHub.app.models.project_collection import ProjectCollection
from portfolioHub.app.models.project import Project
from portfolioHub.app.models.skill import Skill
from pymongo import MongoClient
from config import config

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
    
    #def test_insert_one_already_in_db(self):
    #    project1 = Project(
    #        _id = 1,
    #        firstName = "Juan",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        emailAddress = "juangabrielvasquez11@gmail.com",
    #    )
    #    with pytest.raises(Exception) as exc:
    #        self.collection.insert_one(project1)
    #    assert "duplicate key error" in str(exc.value)
    #
    #def test_insert_one_with_a_non_project_arg(self):
    #    with pytest.raises(ValueError) as ex:
    #        self.collection.insert_one({"_id":7})
    #    assert "Input data expected to be a Project object" in str(ex.value)
#
    #def test_insert_many_complete_projects(self):
    #    projects = [
    #        Project(
    #            _id = 2,
    #            firstName = "Will",
    #            lastName = "Oliver",
    #            emailAddress = "wollie@gmail.com"
    #        ),
    #        Project(
    #            _id = 3,
    #            firstName = "Blake",
    #            lastName = "Dutton",
    #            emailAddress = "bdutt@gmail.com"
    #        )
    #    ]
    #    result = self.collection.insert_many(projects)
    #    assert result[0] == 2
    #    assert result[1] == 3
#
    #def test_insert_many_already_in_db(self):
    #    projects = [
    #       Project(
    #           _id = 2,
    #           firstName = "Will",
    #           lastName = "Oliver",
    #           emailAddress = "wollie@gmail.com"
    #       ),
    #       Project(
    #           _id = 3,
    #           firstName = "Blake",
    #           lastName = "Dutton",
    #           emailAddress = "bdutt@gmail.com"
    #       )
    #   ]
    #    with pytest.raises(Exception) as exc:
    #        self.collection.insert_many(projects)
    #    assert "duplicate key error" in str(exc.value)
#
    #def test_find_one_returns_correct_project(self):
    #    project = self.collection.find_one({"_id":1})
    #    assert project.model_dump(by_alias=True)["_id"] == 1
#
    #def test_find_one_project_not_in_db(self):
    #    project = self.collection.find_one({"_id": 15})
    #    assert project == None
#
    #def test_find_many_returns_correct_projects(self):
    #    projects = self.collection.find_many({"shortBio": ""})
    #    assert all(project.last_name for project in projects)
#
    #def test_find_many_projects_not_in_db(self):
    #    projects = self.collection.find_many({"lastName": "Harper"})
    #    assert projects == None
    #
    #def test_find_many_returns_correct_amt_of_projects(self):
    #    projects = self.collection.find_many({"bio": ""}, 1)
    #    assert len(projects) == 1
#
    #def test_delete_one_project(self):
    #    result = self.collection.delete_one({"_id":3})
    #    assert result == 1
    #
    #def test_delete_one_project_not_in_db(self):
    #    result = self.collection.delete_one({"_id": 15})
    #    assert result == 0
#
    #def test_delete_many_project(self):
    #    result = self.collection.delete_many({"shortBio": ""})
    #    assert result == 2
    #
    #def test_delete_many_project_not_in_db(self):
    #    result = self.collection.delete_many({"lastName": "Thor"})
    #    assert result == 0
#
    #def test_upsert_one_existing_project(self):
    #    project1 = Project(
    #        _id = 1,
    #        firstName = "Juan",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        dateOfBirth = datetime(1996,9,11),
    #        hobbies = [Skill(name="Playing Golf"), Skill(name="Playing Video Games")],
    #        shortBio = "I'm the best of the bests",
    #        bio = "I'm the best",
    #        countryOfBirth = "Dominican Republic",
    #        countryOfResidence = "United States",
    #        emailAddress = "juangabrielvasquez11@gmail.com",
    #        linkedInUrl = "",
    #        gitHubUrl = "",
    #        achievement_ids = [],
    #        project_ids = [],
    #        experience_ids = []
    #    )
    #    filter = {"_id": 1}
    #    result = self.collection.upsert_one(filter, project1)
    #    assert result == 1
#
    #def test_upsert_one_new_project(self):
    #    project1 = Project(
    #        _id = 4,
    #        firstName = "John",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        dateOfBirth = datetime(1996,9,11),
    #        hobbies = [Skill(name="Playing Golf"), Skill(name="Playing Video Games")],
    #        shortBio = "I'm the best of the bests",
    #        bio = "I'm the best",
    #        countryOfBirth = "Dominican Republic",
    #        countryOfResidence = "United States",
    #        emailAddress = "juangvasquez11@gmail.com",
    #        linkedInUrl = "",
    #        gitHubUrl = "",
    #        achievement_ids = [],
    #        project_ids = [],
    #        experience_ids = []
    #    )
    #    filter = {"_id": 4}
    #    result = self.collection.upsert_one(filter, project1)
    #    assert result == 4