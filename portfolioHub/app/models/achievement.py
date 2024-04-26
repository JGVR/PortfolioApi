from typing import List
from .degree import Degree
from .certificate import Certificate
from pydantic import BaseModel, ConfigDict, Field, field_validator

class Achievement(BaseModel):
     # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id = Field(gt=0, alias="personId")
    certificates: List[Certificate]
    degrees: List[Degree]