from typing import List
from pydantic import BaseModel, ConfigDict, Field

class Badge(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    # > name of the badge
    name: str = Field(max_length=100)
    # > link to an image/icon
    url: str
