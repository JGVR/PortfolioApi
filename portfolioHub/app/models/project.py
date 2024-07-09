from typing import List
from pydantic import BaseModel, ConfigDict, Field, field_validator
from ..services.reference_integrity_checker import ReferenceIntegrityChecker
from .badge import Badge

class Project(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    user_id: int = Field(gt=0, alias="userId")
    name: str = Field(max_length=250)
    description: str = Field(max_length=1000)
    badge: List[Badge] = Field(alias="badges")
    images: List[str] = Field(default=[])
    url: str = Field(default="")