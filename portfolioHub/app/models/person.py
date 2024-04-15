from typing import List
from pydantic import BaseModel, ConfigDict, Field
from datetime import date

class Person(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    # > id should be greater than 0
    id: int = Field(gt=0, alias="_id")
    first_name: str = Field(min_length=1, max_length=250, alias="firstName")
    middle_name: str = Field(max_length=250, default="", alias="middleName")
    last_name: str = Field(min_length=1, max_length=250, alias="lastName")
    date_of_birth: date = Field(alias="dateOfBirth")
    hobbies: List[str] = Field(default=[])
    short_bio: str = Field(min_length=50, max_length=350, alias="shortBio")
    bio: str = Field(max_length=1000)
    country_of_birth: str = Field(default="", alias="countryOfBirth")
    country_of_residence: str = Field(default="", alias="countryOfResidence")
    # > could use EmailStr pydantic type instead
    email_address: str = Field(pattern=r"^[\w,-]+@[a-zA-Z].{2,}$", alias="emailAddress")
    linkedIn_url: str = Field(default="", alias="linkedInUrl")
    gitHub_url: str = Field(default="", alias="gitHubUrl")
    achievement_ids: List[int] = Field(default=None)
    project_ids: List[int] = Field(default=None)
    experience_ids: List[int] = Field(default=None)