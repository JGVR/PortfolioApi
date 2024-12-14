from .edu_entity import EduEntity
from pydantic import Field, BaseModel, ConfigDict

class Degree(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, str_to_lower=True, extra='forbid', populate_by_name=True)

    # > properties
    name: str = Field(max_length=150)
    description: str = Field(max_length=1000, default="")
    url: str = Field(default="")
    school: EduEntity