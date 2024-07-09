from typing import List
from .degree import Degree
from .certificate import Certificate
from pydantic import BaseModel, ConfigDict, Field

class Achievement(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    # > properties
    user_id: int = Field(gt=0, alias="userId")
    certificates: List[Certificate]
    degrees: List[Degree]