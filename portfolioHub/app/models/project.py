from typing import List
from pydantic import BaseModel, ConfigDict, Field
from skill import Skill

class Project(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id: int = Field(gt=0, alias="personId")
    name: str = Field(min_length=5 ,max_length=250)
    description: str = Field(min_length=50, max_length=250)
    skills: List[Skill] = Field(default=[])
    images: List[str] = Field(default=[])
    url: str = Field(default="")