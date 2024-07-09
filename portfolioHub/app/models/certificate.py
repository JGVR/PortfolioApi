from .edu_entity import EduEntity
from pydantic import Field, BaseModel, ConfigDict

class Certificate(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    name: str = Field(max_length=150)
    url: str = Field(default="")
    description: str = Field(max_length=150, default="")
    platform: EduEntity