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