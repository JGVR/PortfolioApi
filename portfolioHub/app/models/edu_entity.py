from pydantic import BaseModel, ConfigDict, Field

class EduEntity(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    # > properties
    name: str = Field(max_length=150)