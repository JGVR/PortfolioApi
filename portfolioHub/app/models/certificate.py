from .edu_entity import EduEntity
from pydantic import Field, BaseModel, ConfigDict

class Certificate(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid', populate_by_name=True)

    name: str = Field(max_length=150)
    description: str = Field(max_length=150, default="")
    url: str = Field(default="")
    platform: EduEntity