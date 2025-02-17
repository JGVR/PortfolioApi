from typing import List, Any, Dict
from pymongo.collection import Collection
from .db_handler import DbHandler
from .profile import Profile
from .hobby import Hobby
from .skill import Skill
from ..utils.type import Type
from datetime import datetime
from bson import ObjectId

class ProfileHandler(DbHandler):
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, profiles: List[Profile]) -> List[ObjectId]:
        if not all(isinstance(profile, Profile) for profile in profiles):
            raise ValueError("Input data expected to be a list of Profile")
        
        profiles_data = []
        for profile in profiles:
            data = {
                '_id': ObjectId(),
                'type': Type.PROFILE.value,
                'createdAt': datetime.today(),
                'userId': profile.user_id,
                'firstName': profile.first_name,
                'lastName': profile.last_name,
                'dateOfBirth': profile.date_of_birth,
                'hobbies': [hobby.name for hobby in profile.hobbies],
                'skills': [skill.name for skill in profile.skills],
                'shortBio': profile.short_bio,
                'bio': profile.bio,
                'countryOfBirth': profile.country_of_birth,
                'countryOfResidence': profile.country_of_residence,
                'linkedInUrl': profile.linkedIn_url,
                'gitHubUrl': profile.gitHub_url
            }
            profiles_data.append(data)

        result = self.collection.insert_many(profiles_data).inserted_ids
        return result
    
    def find(self, filter: Dict[str,Any], max: int = 5, skip: int = 0) -> List[Profile]:
        print(filter)
        cursor = self.collection.find(filter).skip(skip).limit(max)
        profiles = []

        for doc in cursor:
            profile = Profile(
                user_id = doc["userId"],
                first_name = doc["firstName"],
                last_name = doc["lastName"],
                date_of_birth = doc["dateOfBirth"],
                hobbies = [Hobby(name=hobby) for hobby in doc["hobbies"]],
                skills = [Skill(name=skill) for skill in doc["skills"]],
                short_bio = doc["shortBio"],
                bio = doc["bio"],
                country_of_birth = doc["countryOfBirth"],
                country_of_residence = doc["countryOfResidence"],
                linkedIn_url = doc["linkedInUrl"],
                gitHub_url = doc["gitHubUrl"]
            )

            profiles.append(profile)
        

        if len(profiles) > 0:
            return profiles
        return None
    
    def delete(self, filter: Dict[str,Any]) -> Dict[str,int]:
        return {"count":self.collection.delete_many(filter).deleted_count}