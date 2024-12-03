import pytest
from datetime import datetime
from portfolioHub.app.models.profile import Profile
from portfolioHub.app.models.profile_handler import ProfileHandler
from portfolioHub.app.models.hobby import Hobby
from portfolioHub.app.models.skill import Skill
from portfolioHub.app.config import config
from pymongo import MongoClient
from bson import ObjectId

class TestProfileCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolioHub"]
    collection = db["userPortfolio"]
    handler = ProfileHandler(collection)

    def test_insert_one_profile(self):
        user_profile = Profile(
            user_id=1, 
            first_name="Juan",
            last_name="Vasquez",
            date_of_birth=datetime(2024, 9, 11),
            hobbies=[
                Hobby(name="coding"),
                Hobby(name="golfing")
            ],
            skills=[
                Skill(name="python"),
                Skill(name="SSIS")
            ],
            short_bio="Testing Short Bio",
            bio="testing bio",
            country_of_birth="Dominican Republic",
            country_of_residence="United States",
        )
        profile_ids = self.handler.insert([user_profile])
        assert isinstance(profile_ids[0], ObjectId)
    
    def test_find_one_profile(self):
        filter = {"userId": 1}
        result = self.handler.find(filter)
        assert result[0].first_name == "Juan"