from pydantic import BaseModel, ConfigDict, Field

class Entity(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    name: str = Field(min_length=5, max_length=250)