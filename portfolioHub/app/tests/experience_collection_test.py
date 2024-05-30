import pytest
from portfolioHub.app.models.experience_collection import ExperienceCollection
from portfolioHub.app.models.experience import Experience
from portfolioHub.app.models.company import Company
from portfolioHub.app.config import config
from pymongo import MongoClient
from datetime import datetime

class TestExperienceCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolio"]
    collection = ExperienceCollection(db["experience"])

    def test_insert_one_with_a_non_existent_person(self):
        with pytest.raises(ValueError) as exc_info:
            experience1 = Experience(
                _id = 6,
                personId = 10,
                projectIds = [],
                company = Company(name="K-VA-T Food Stores"),
                jobTitle = "Software Developer I",
            )
        assert "The person Id: 10 was not found in the persons collection. Please make sure the person exists before assigning an experience to a person." in str(exc_info.value)

    def test_insert_one_experience(self):
        experience1 = Experience(
            _id = 1,
            personId = 1,
            projectIds = [],
            company = Company(name="K-VA-T Food Stores"),
            jobTitle = "Software Developer I",
        )
        result = self.collection.insert_one(experience1)
        assert result == 1

    def test_insert_one_already_in_db(self):
        experience1 = Experience(
            _id = 1,
            personId = 1,
            projectIds = [],
            company = Company(name="K-VA-T Food Stores"),
            jobTitle = "Software Developer I",
        )
        with pytest.raises(Exception) as exc:
            self.collection.insert_one(experience1)
        assert "duplicate key error" in str(exc.value)
    
    def test_insert_one_with_a_non_experience_arg(self):
        with pytest.raises(ValueError) as ex:
            self.collection.insert_one({"_id":7})
        assert "Input data expected to be a Experience object" in str(ex.value)

    def test_insert_many_complete_experiences(self):
        experiences = [
            Experience(
                _id = 2,
                personId = 1,
                projectIds = [1, 2],
                company = Company(name="Test Company"),
                jobTitle = "Software Developer II"
            ),
            Experience(
                _id = 3,
                personId = 1,
                projectIds = [3],
                company = Company(name="Test Comp 2"),
                jobTitle = "Software Developer III"
            )
        ]
        result = self.collection.insert_many(experiences)
        assert result[0] == 2
        assert result[1] == 3

    def test_insert_many_already_in_db(self):
        experiences = [
            Experience(
                _id = 2,
                personId = 1,
                projectIds = [1, 2],
                company = Company(name="Test Company"),
                jobTitle = "Software Developer II"
            ),
            Experience(
                _id = 3,
                personId = 1,
                projectIds = [3],
                company = Company(name="Test Comp 2"),
                jobTitle = "Software Developer III"
            )
        ]
        with pytest.raises(Exception) as exc:
            self.collection.insert_many(experiences)
        assert "duplicate key error" in str(exc.value)

    def test_find_one_returns_correct_experience(self):
        experience = self.collection.find_one({"_id":1})
        assert experience.model_dump(by_alias=True)["_id"] == 1

    def test_find_one_experience_not_in_db(self):
        experience = self.collection.find_one({"_id": 15})
        assert experience == None

    def test_find_many_returns_correct_experiences(self):
        experiences = self.collection.find_many({"personId": 1})
        assert all(experience.person_id for experience in experiences)

    def test_find_many_experiences_not_in_db(self):
        experiences = self.collection.find_many({"lastName": "Harper"})
        assert experiences == None
    
    def test_find_many_returns_correct_amt_of_experiences(self):
        experiences = self.collection.find_many({"personId": 1}, 3)
        assert len(experiences) == 3

    def test_delete_one_experience(self):
        result = self.collection.delete_one({"_id":3})
        assert result == 1
    
    def test_delete_one_experience_not_in_db(self):
        result = self.collection.delete_one({"_id": 15})
        assert result == 0

    def test_delete_many_experience(self):
        result = self.collection.delete_many({"personId": 1})
        assert result == 2
    
    def test_delete_many_experience_not_in_db(self):
        result = self.collection.delete_many({"lastName": "Thor"})
        assert result == 0

    def test_upsert_one_existing_experience(self):
        experience1 = Experience(
            _id = 4,
            personId = 1,
            projectIds = [],
            company = Company(name="Test Comp 4"),
            jobTitle = "Software Developer IV",
            jobDescription="test job description",
            startDate= datetime(2022,2,14),
            endDate=None
        )
        filter = {"_id": 4}
        result = self.collection.upsert_one(filter, experience1)
        assert result == 4

    def test_upsert_one_new_experience(self):
        experience1 = Experience(
            _id = 5,
            personId = 1,
            projectIds = [],
            company = Company(name="Test Comp 5"),
            jobTitle = "Software Developer IV",
            jobDescription="test job description",
            startDate= datetime(2022,2,14),
            endDate=None
        )
        filter = {"_id": 5}
        result = self.collection.upsert_one(filter, experience1)
        assert result == 5