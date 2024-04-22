import pytest
from datetime import datetime
from portfolioHub.app.models.person_collection import PersonCollection
from portfolioHub.app.models.person import Person
from portfolioHub.app.models.hobby import Hobby
from pymongo import MongoClient

class TestPersonCollection:
    cluster = MongoClient("mongodb+srv://jv_admin:Th0r3s3lDi0sDelTrueno1130!@portfolio.jmd2tdg.mongodb.net/?retryWrites=true&w=majority&appName=Portfolio")
    db = cluster["portfolio"]
    collection = PersonCollection(db["persons"])
    filter_1 = {"_id": 1}
    filter_2 = {"firstName": "Juan"}
    filter_3 = {"emailAddress": "juangabrielvasquez11@gmail.com"}
    filter_4 = {"fruit": "mango"}
    
    def test_find_one_returns_a_person(self):
        person = self.collection.find_one(self.filter_1)
        assert isinstance(person, Person)
  
    def test_find_one_returns_correct_person(self):
        person = self.collection.find_one(self.filter_1)
        """expected_person = {
            "_id": 1,
            "firstName": "Juan",
            "middleName": "Gabriel",
            "lastName": "Vasquez",
            "dateOfBirth": datetime(1996,9,11),
            "hobbies": [Hobby("Playing Golf"), Hobby("Reading"), Hobby("Coding")],
            "shortBio": "Tech-savvy professional with progressive experience in designing, developing, and delivering cutting-edge software solutions.",
            "bio": "",
            "countryOfBirth": "Dominican Republic",
            "countryOfResidence": "United States",
            "emailAddress": "juangabrielvasquez11@gmail.com",
            "linkedInUrl": "",
            "gitHubUrl": "",
            "achievement_ids": [],
            "project_ids": [],
            "experience_ids": []
        }"""
        assert 1 == person.model_dump(by_alias=True)["_id"]