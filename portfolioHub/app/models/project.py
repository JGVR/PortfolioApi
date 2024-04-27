from typing import List
from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationError
from .skill import Skill
from ..services.reference_integrity_checker import ReferenceIntegrityChecker
from .person_collection import PersonCollection
from config import config
from pymongo import MongoClient

class Project(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id: int = Field(gt=0, alias="personId")
    name: str = Field(min_length=5 ,max_length=250)
    description: str = Field(max_length=250)
    skills: List[Skill] = Field(default=[])
    images: List[str] = Field(default=[])
    url: str = Field(default="")

    #Validate person exists before inserting project
    @field_validator('person_id', mode='before')
    def check_person_id(cls, id) -> int:
        db = MongoClient(config.atlas_conn_str)["portfolio"]
        collection = PersonCollection(db['persons'])
        exists = ReferenceIntegrityChecker.check_id_existence(id, collection)
        if exists == False:
            raise ValueError(f"The person Id: {id} was not found in the persons collections. Please make sure the person exists before assigning a project to a person.")
        return id