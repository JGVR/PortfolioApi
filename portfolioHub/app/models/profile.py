from typing import List
from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import datetime
from .hobby import Hobby
from .skill import Skill

class Profile(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, str_to_lower=True, extra='forbid', populate_by_name=True)

    # > properties
    user_id: int = Field(gt=0, alias="userId")
    first_name: str = Field(min_length=1, max_length=250, alias="firstName")
    last_name: str = Field(min_length=1, max_length=250, alias="lastName")
    date_of_birth: datetime = Field(alias="dateOfBirth", default=None)
    hobbies: List[Hobby] = Field(default=[])
    skills: List[Skill] = Field(default=[])
    short_bio: str = Field(max_length=350, alias="shortBio", default="")
    bio: str = Field(max_length=1000, default="")
    country_of_birth: str = Field(default="", alias="countryOfBirth")
    country_of_residence: str = Field(default="", alias="countryOfResidence")
    linkedIn_url: str = Field(default="", alias="linkedInUrl")
    gitHub_url: str = Field(default="", alias="gitHubUrl")