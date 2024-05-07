import pytest
from datetime import datetime
from portfolioHub.app.models.person_collection import PersonCollection
from portfolioHub.app.models.person import Person
from portfolioHub.app.models.hobby import Hobby
from portfolioHub.app.config import config
from pymongo import MongoClient

class TestPersonCollection:
    cluster = MongoClient(config.atlas_conn_str)
    db = cluster["portfolio"]
    collection = PersonCollection(db["persons"])

    def test_insert_one_person(self):
        data = {
            "_id": 2,
	        "firstName": "Juan",
            "lastName": "Vasquez",
            "emailAddress": "juangabrielvasquez11@gmail.com"
        }
        person1 = Person(**data)
        result = self.collection.insert_one(person1)
        assert result == 2
    
    #def test_insert_one_already_in_db(self):
    #    person1 = Person(
    #        _id = 1,
    #        firstName = "Juan",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        emailAddress = "juangabrielvasquez11@gmail.com",
    #    )
    #    with pytest.raises(Exception) as exc:
    #        self.collection.insert_one(person1)
    #    assert "duplicate key error" in str(exc.value)
    #
    #def test_insert_one_with_a_non_person_arg(self):
    #    with pytest.raises(ValueError) as ex:
    #        self.collection.insert_one({"_id":7})
    #    assert "Input data expected to be a Person object" in str(ex.value)
#
    #def test_insert_many_complete_persons(self):
    #    persons = [
    #        Person(
    #            _id = 2,
    #            firstName = "Will",
    #            lastName = "Oliver",
    #            emailAddress = "wollie@gmail.com"
    #        ),
    #        Person(
    #            _id = 3,
    #            firstName = "Blake",
    #            lastName = "Dutton",
    #            emailAddress = "bdutt@gmail.com"
    #        )
    #    ]
    #    result = self.collection.insert_many(persons)
    #    assert result[0] == 2
    #    assert result[1] == 3
#
    #def test_insert_many_already_in_db(self):
    #    persons = [
    #       Person(
    #           _id = 2,
    #           firstName = "Will",
    #           lastName = "Oliver",
    #           emailAddress = "wollie@gmail.com"
    #       ),
    #       Person(
    #           _id = 3,
    #           firstName = "Blake",
    #           lastName = "Dutton",
    #           emailAddress = "bdutt@gmail.com"
    #       )
    #   ]
    #    with pytest.raises(Exception) as exc:
    #        self.collection.insert_many(persons)
    #    assert "duplicate key error" in str(exc.value)
#
    #def test_find_one_returns_correct_person(self):
    #    person = self.collection.find_one({"_id":1})
    #    assert person.model_dump(by_alias=True)["_id"] == 1
#
    #def test_find_one_person_not_in_db(self):
    #    person = self.collection.find_one({"_id": 15})
    #    assert person == None
#
    #def test_find_many_returns_correct_persons(self):
    #    persons = self.collection.find_many({"shortBio": ""})
    #    assert all(person.last_name for person in persons)
#
    #def test_find_many_persons_not_in_db(self):
    #    persons = self.collection.find_many({"lastName": "Harper"})
    #    assert persons == None
    #
    #def test_find_many_returns_correct_amt_of_persons(self):
    #    persons = self.collection.find_many({"bio": ""}, 1)
    #    assert len(persons) == 1
#
    #def test_delete_one_person(self):
    #    result = self.collection.delete_one({"_id":3})
    #    assert result == 1
    #
    #def test_delete_one_person_not_in_db(self):
    #    result = self.collection.delete_one({"_id": 15})
    #    assert result == 0
#
    #def test_delete_many_person(self):
    #    result = self.collection.delete_many({"shortBio": ""})
    #    assert result == 2
    #
    #def test_delete_many_person_not_in_db(self):
    #    result = self.collection.delete_many({"lastName": "Thor"})
    #    assert result == 0
#
    #def test_upsert_one_existing_person(self):
    #    person1 = Person(
    #        _id = 1,
    #        firstName = "Juan",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        dateOfBirth = datetime(1996,9,11),
    #        hobbies = [Hobby(name="Playing Golf"), Hobby(name="Playing Video Games")],
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
    #    result = self.collection.upsert_one(filter, person1)
    #    assert result == 1
#
    #def test_upsert_one_new_person(self):
    #    person1 = Person(
    #        _id = 4,
    #        firstName = "John",
    #        middleName = "Gabriel",
    #        lastName = "Vasquez",
    #        dateOfBirth = datetime(1996,9,11),
    #        hobbies = [Hobby(name="Playing Golf"), Hobby(name="Playing Video Games")],
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
    #    result = self.collection.upsert_one(filter, person1)
    #    assert result == 4