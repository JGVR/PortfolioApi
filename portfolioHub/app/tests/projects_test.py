import pytest
from datetime import datetime
from portfolioHub.app.models.project_handler import ProjectHandler
from portfolioHub.app.models.project import Project
from portfolioHub.app.models.badge import Badge
from pymongo import MongoClient
from portfolioHub.app.config import config
from pydantic import ValidationError as PValidationError
from bson import ObjectId


class TestProjectCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolioHub"]
    collection = db["userPortfolio"]
    handler = ProjectHandler(collection)

    def test_insert_one_project(self):
        project = Project(
            userId=1,
            name="STBC Mobile App",
            description="Testing the project model",
            badges=[
                Badge(name="Python", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"),
                Badge(name="Javascript", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png")
            ],
            images=[
                "https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"
            ]
        )
        result = self.handler.insert([project])
        assert isinstance(result[0], ObjectId)

    def test_insert_many_projects(self):
        projects = [
            Project(
                userId=3,
                name="Portfolio App",
                description="Testing the project model",
                badges=[
                    Badge(name="Python", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"),
                    Badge(name="Javascript", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png")
                ],
                images=[
                    "https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"
                ]
            ),
            Project(
                userId=2,
                name="STBC Admin Page",
                description="Testing the project model",
                badges=[
                    Badge(name="Python", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"),
                    Badge(name="Javascript", url="https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png")
                ],
                images=[
                    "https://stbc.blob.core.windows.net/stbc-mobile-app-images/strong-tower-kids.png"
                ]
            )
        ]
        result = self.handler.insert(projects)
        assert all(isinstance(id, ObjectId) for id in result)
    
    def test_find_one_project(self):
        filter = {"name": "STBC Mobile App"}
        result = self.handler.find(filter)
        assert result[0].name == "STBC Mobile App"
    
    def test_delete_one_project(self):
        filter = {"name": "STBC Mobile App"}
        result = self.handler.delete(filter)
        assert result["count"] == 1

    def test_delete_many_projects(self):
        filter = {"badges": {"$elemMatch": {
            "name": "Python"
        }}}
        result = self.handler.delete(filter)
        assert result["count"] == 2