from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    id: int
    first_name: str
    middle_name: str
    last_name: str
    date_of_birth: date
    hobbies: List[str]
    short_bio: str
    bio: str
    country_of_birth: str
    country_of_residence: str
    email_address: str
    linkedIn_url: str
    gitHub_url: str
    achievement_ids: List[int]
    project_ids: List[int]
    experience_ids: List[int]