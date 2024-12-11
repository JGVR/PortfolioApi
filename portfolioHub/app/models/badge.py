from typing import List
from pydantic import BaseModel, ConfigDict, Field

class Badge(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, str_to_lower=True, extra='forbid', populate_by_name=True)
    
    # > properties
    name: str = Field(max_length=100)
    url: str
