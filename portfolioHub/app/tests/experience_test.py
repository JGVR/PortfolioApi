import pytest
from portfolioHub.app.models.experience_handler import ExperienceHandler
from portfolioHub.app.models.experience import Experience
from portfolioHub.app.models.company import Company
from portfolioHub.app.config import config
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

class TestExperienceCollection:
    cluster = cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolioHub"]
    collection = db["userPortfolio"]
    handler = ExperienceHandler(collection)

    def test_insert_one_experience(self):
        experience = Experience(
            userId=1,
            jobTitle="Software Dev",
            jobDescription="testing job desc",
            company=Company(name="K-VA-T Food Stores"),
            startDate=datetime(2022, 2, 14),
            endDate=datetime(2024,9,11)
        )
        result = self.handler.insert([experience])
        assert isinstance(result[0], ObjectId)
    
    def test_insert_many_experiences(self):
        experiences = [
            Experience(
                userId=3,
                jobTitle="Software Developer",
                jobDescription="testing job desc",
                company=Company(name="K-VA-T Food Stores"),
                startDate=datetime(2022, 2, 14),
                endDate=datetime(2024,9,11)
            ),
            Experience(
                userId=2,
                jobTitle="Production Supervisor",
                jobDescription="testing job desc 2",
                company=Company(name="The Robinette Company"),
                startDate=datetime(2020,7,12),
                endDate=datetime(2022,2,14)
            )
        ]
        result = self.handler.insert(experiences)
        assert all(isinstance(id, ObjectId) for id in result)

    def test_find_one_experience(self):
        filter = {"jobTitle": "Software Dev"}
        result = self.handler.find(filter)
        assert result[0].job_title == "Software Dev"

    def test_find_many_experience(self):
        filter = {"company": "K-VA-T Food Stores"}
        result = self.handler.find(filter)
        assert result[0].company.name == "K-VA-T Food Stores"

    def test_delete_one_experience(self):
        filter = {"jobTitle": "Production Supervisor"}
        result = self.handler.delete(filter)
        assert result["count"] == 1

    def test_delete_many_experiences(self):
        filter = {"company": "K-VA-T Food Stores"}
        result = self.handler.delete(filter)
        assert result["count"] == 2