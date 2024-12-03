import pytest
from portfolioHub.app.models.user import User
from portfolioHub.app.models.user_handler import UserHandler
from portfolioHub.app.config import config
from pymongo import MongoClient
from bson import ObjectId

class TestUserCollection:
    cluster = MongoClient("mongodb+srv://jv_admin:Th0r3s3lDi0sDelTrueno1130!!@portfolio.jmd2tdg.mongodb.net/?retryWrites=true&w=majority&appName=Portfolio")
    db = cluster["portfolioHub"]
    collection = db["userPortfolio"]
    handler = UserHandler(collection)

    def test_insert_one_user(self):
        user = User(userId=1, emailAddress="juangabrielvasquez11@gmail.com")
        user_ids = self.handler.insert([user])
        assert isinstance(user_ids[0], ObjectId)

    def test_insert_many_users(self):
        users = [
            User(userId=2, emailAddress="juangabrielvasquez11@gmail.com"),
            User(userId=3, emailAddress="juangabrielvasquez11@gmail.com"),
            User(userId=4, emailAddress="juangabrielvasquez11@gmail.com")
        ]
        user_ids = self.handler.insert(users)
        assert all(isinstance(id, ObjectId) for id in user_ids)
    
    def test_find_one_returns_correct_user(self):
        user = self.handler.find({"userId":1})
        assert user[0].model_dump(by_alias=True)["userId"] == 1

    def test_delete_one_user(self):
        user = self.handler.delete({"userId": 1})
        assert user["count"] == 1
    
    def test_delete_many_users(self):
        user = self.handler.delete({"emailAddress": "juangabrielvasquez11@gmail.com"})
        assert user["count"] == 3