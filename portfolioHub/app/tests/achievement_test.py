import pytest
from portfolioHub.app.models.achievement_handler import AchievementHandler
from portfolioHub.app.models.achievement import Achievement
from portfolioHub.app.models.certificate import Certificate
from portfolioHub.app.models.degree import Degree
from portfolioHub.app.models.edu_entity import EduEntity
from portfolioHub.app.config import config
from pymongo import MongoClient
from bson import ObjectId

class TestAchievementCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolioHub"]
    collection = db["userPortfolio"]
    handler = AchievementHandler(collection)

    def test_insert_one_achievement(self):
        achievement = Achievement(
            userId = 10,
            certificates = [
                Certificate(
                    name="Computer Science",
                    description = "Codecademy Computer Science course",
                    platform = EduEntity(name="Codecademy")
                )
            ],
            degrees = [
                Degree(
                    name = "Business Administration & Computer Science",
                    description = "Double Major in Business Administration & Computer Information System",
                    school = EduEntity(name="Milligan University") 
                )
            ]
        )
        result = self.handler.insert(achievement)
        assert isinstance(result[0], ObjectId)
    
    def test_insert_many_achievement(self):
        achievement = Achievement(
                userId = 10,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = EduEntity(name="Codecademy")
                    ),
                    Certificate(
                        name="Math for ML",
                        description = "Math for Machiene Learning",
                        platform = EduEntity(name="Coursera")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = EduEntity(name="Milligan University") 
                    ),
                    Degree(
                        name = "Computer Science AI",
                        description = "Master Degreen in Computer Science AI",
                        school = EduEntity(name="ETSU") 
                    )
                ]
            )
        result = self.handler.insert(achievement)
        assert isinstance(result[0], ObjectId)

    def test_find_one_achievement(self):
        filter = {"name": "Computer Science"}
        result = self.handler.find(filter)
        assert result.certificates[0].name == "Computer Science"

    def test_delete_one_achievement(self):
        filter = {"name": "Business Administration & Computer Science"}
        result = self.handler.delete(filter)
        assert result["count"] == 1