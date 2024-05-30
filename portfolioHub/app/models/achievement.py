from typing import List
from .degree import Degree
from .certificate import Certificate
from pydantic import BaseModel, ConfigDict, Field, field_validator
from ..services.reference_integrity_checker import ReferenceIntegrityChecker

class Achievement(BaseModel):
     # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id: int = Field(gt=0, alias="personId")
    certificates: List[Certificate]
    degrees: List[Degree]
    
    @field_validator('person_id', mode="before")
    def check_person_id(cls, id) -> int:
        exists = ReferenceIntegrityChecker.check_id_existence("portfolio", "persons",id)
        if exists == False:
            raise ValueError(f"The person Id: {id} was not found in the persons collection. Please make sure the person exists before assigning an achievement to a person.")
        return id