from typing import List
from .degree import Degree
from .certificate import Certificate
from pydantic import BaseModel, ConfigDict, Field

class Achievement(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, str_to_lower=True, extra='forbid', populate_by_name=True)

    # > properties
    user_id: int = Field(gt=0, alias="userId")
    certificates: List[Certificate]
    degrees: List[Degree]