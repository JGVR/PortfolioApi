import pytest
from portfolioHub.app.models.achievement_collection import AchievementCollection
from portfolioHub.app.models.achievement import Achievement
from portfolioHub.app.models.certificate import Certificate
from portfolioHub.app.models.degree import Degree
from portfolioHub.app.models.school import School
from config import config
from pymongo import MongoClient

class TestAchievementCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolio"]
    collection = AchievementCollection(db["achievements"])

    def test_insert_one_with_a_non_existent_person(self):
        with pytest.raises(ValueError) as exc_info:
            achievement1 = Achievement(
                _id = 1,
                personId = 10,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            )
        assert "The person Id: 10 was not found in the persons collection. Please make sure the person exists before assigning an achievement to a person." in str(exc_info.value)

    def test_insert_one_achievement(self):
        achievement1 = Achievement(
                _id = 1,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            )
        result = self.collection.insert_one(achievement1)
        assert result == 1
    
    def test_insert_one_already_in_db(self):
        achievement1 = Achievement(
                _id = 1,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            )
        with pytest.raises(Exception) as exc:
            self.collection.insert_one(achievement1)
        assert "duplicate key error" in str(exc.value)
    
    def test_insert_one_with_a_non_achievement_arg(self):
        with pytest.raises(ValueError) as ex:
            self.collection.insert_one({"_id":7})
        assert "Input data expected to be a Achievement object" in str(ex.value)

    def test_insert_many_complete_achievements(self):
        achievements = [Achievement(
                _id = 2,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            ),
            Achievement(
                _id = 3,
                personId = 1,
                certificates = [
                    Certificate(
                        name = "Web Development",
                        description = "Codecademy Web Development course",
                        platform = School(name="Codecademy")
                        ),
                    Certificate(
                    name = "React Beginner",
                    description = "Codecademy React course",
                    platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Accounting",
                        type = "Bachelor of Science",
                        description = "Bachelor of Science in Accounting",
                        school = School(name="Milligan University")
                    )
                ]
            )]
        result = self.collection.insert_many(achievements)
        assert result[0] == 2
        assert result[1] == 3

    def test_insert_many_already_in_db(self):
        achievements = [Achievement(
                _id = 2,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            ),
            Achievement(
                _id = 3,
                personId = 1,
                certificates = [
                    Certificate(
                        name = "Web Development",
                        description = "Codecademy Web Development course",
                        platform = School(name="Codecademy")
                        ),
                    Certificate(
                    name = "React Beginner",
                    description = "Codecademy React course",
                    platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Accounting",
                        type = "Bachelor of Science",
                        description = "Bachelor of Science in Accounting",
                        school = School(name="Milligan University")
                    )
                ]
            )]
        with pytest.raises(Exception) as exc:
            self.collection.insert_many(achievements)
        assert "duplicate key error" in str(exc.value)

    def test_find_one_returns_correct_achievement(self):
        achievement = self.collection.find_one({"_id":1})
        assert achievement.model_dump(by_alias=True)["_id"] == 1

    def test_find_one_achievement_not_in_db(self):
        achievement = self.collection.find_one({"_id": 15})
        assert achievement == None

    def test_find_many_returns_correct_achievements(self):
        achievements = self.collection.find_many({"personId": 1})
        assert all(achievement.person_id for achievement in achievements)

    def test_find_many_achievements_not_in_db(self):
        achievements = self.collection.find_many({"personId": 5})
        assert achievements == None
    
    def test_find_many_returns_correct_amt_of_achievements(self):
        achievements = self.collection.find_many({"personId": 1}, 3)
        assert len(achievements) == 3

    def test_delete_one_achievement(self):
        result = self.collection.delete_one({"_id":3})
        assert result == 1
    
    def test_delete_one_achievement_not_in_db(self):
        result = self.collection.delete_one({"_id": 15})
        assert result == 0

    def test_delete_many_achievement(self):
        result = self.collection.delete_many({"personId": 1})
        assert result == 2
    
    def test_delete_many_achievement_not_in_db(self):
        result = self.collection.delete_many({"lastName": "Thor"})
        assert result == 0

    def test_upsert_one_existing_achievement(self):
        achievement1 = Achievement(
                _id = 1,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    ),
                    Certificate(
                        name="Ruby On Rails Beginner",
                        description = "Codecademy Ruby On Rails course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            )
        filter = {"_id": 1}
        result = self.collection.upsert_one(filter, achievement1)
        assert result == 1

    def test_upsert_one_new_achievement(self):
        achievement1 =Achievement(
                _id = 5,
                personId = 1,
                certificates = [
                    Certificate(
                        name="Computer Science",
                        description = "Codecademy Computer Science course",
                        platform = School(name="Codecademy")
                    ),
                    Certificate(
                        name="C# Beginner",
                        description = "Codecademy C# course",
                        platform = School(name="Codecademy")
                    )
                ],
                degrees = [
                    Degree(
                        name = "Business Administration & Computer Science",
                        type = "Bachelor of Science",
                        description = "Double Major in Business Administration & Computer Information System",
                        school = School(name="Milligan University") 
                    )
                ]
            )
        filter = {"_id": 5}
        result = self.collection.upsert_one(filter, achievement1)
        assert result == 5