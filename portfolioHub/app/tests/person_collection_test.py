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
    filter_2 = {"lastName": "Vasquez"}
    person1 = Person(
        _id = 6,
        firstName = "Will",
        lastName = "Oliver",
        emailAddress = "wollie@gmail.com"
    )
    person2 = Person(
        _id = 7,
        firstName = "Blake",
        lastName = "Dutton",
        emailAddress = "bdutt@gmail.com"
    )
    person3 = Person(
        _id = 8,
        firstName = "Allison",
        middleName = "Brooke",
        lastName = "Vasquez",
        dateOfBirth = datetime(1994,4,4),
        hobbies = ["Playing Basketball"],
        shortBio = "",
        bio = "",
        countryOfBirth = "United States",
        countryOfResidence = "United States",
        emailAddress = "avasquez@gmail.com",
        linkedInUrl = "",
        gitHubUrl = "",
        achievement_ids = [],
        project_ids = [],
        experience_ids = []
    )
    person4 = Person(
        _id = 9,
        firstName = "Michelle",
        middleName = "",
        lastName = "Littleton",
        dateOfBirth = datetime(1994,4,4),
        hobbies = ["Working out"],
        shortBio = "",
        bio = "",
        countryOfBirth = "United States",
        countryOfResidence = "United States",
        emailAddress = "mlittle@gmail.com",
        linkedInUrl = "",
        gitHubUrl = "",
        achievement_ids = [],
        project_ids = [],
        experience_ids = []
    )
    
    def test_find_one_returns_a_person(self):
        person = self.collection.find_one(self.filter_1)
        assert isinstance(person, Person)
  
    def test_find_one_returns_correct_person(self):
        person = self.collection.find_one(self.filter_1)
        assert 1 == person.model_dump(by_alias=True)["_id"]

    def test_find_one_raises_type_error_on_no_args(self):
        with pytest.raises(TypeError):
            self.collection.find_one()

    def test_find_many_returns_a_list_of_person(self):
        persons = self.collection.find_many(self.filter_2)
        assert all(isinstance(person, Person) for person in persons)

    def test_find_many_returns_correct_persons(self):
        persons = self.collection.find_many(self.filter_2)
        assert all(person.last_name for person in persons)

    def test_find_many_raises_type_error_on_no_args(self):
        with pytest.raises(TypeError):
            self.collection.find_many()
    
    def test_find_many_returns_correct_amt_of_persons(self):
        persons = self.collection.find_many(self.filter_2, 2)
        assert len(persons) == 2

    #def test_insert_one_person_with_only_required_prop(self):
    #    result = self.collection.insert_one(self.person1)
    #    assert result == True

    #def test_insert_one_complete_person(self):
    #    result = self.collection.insert_one(self.person2)
    #    assert result == True

    def test_insert_one_raises_type_error_on_no_args(self):
        with pytest.raises(TypeError):
            self.collection.insert_one()
    
    def test_insert_one_with_a_non_person_arg(self):
        with pytest.raises(ValueError) as ex:
            self.collection.insert_one({"_id":7})
        assert "Input data expected to be a Person object" in str(ex.value)
    
    #def test_insert_many_persons_with_only_required_prop(self):
    #    result = self.collection.insert_many([self.person1, self.person2])
    #    assert result == True

    #def test_insert_many_complete_persons(self):
    #    result = self.collection.insert_many([self.person3, self.person4])
    #    assert result == True

    def test_insert_many_raises_type_error_on_no_args(self):
        with pytest.raises(TypeError):
            self.collection.insert_many()