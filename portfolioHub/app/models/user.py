from pydantic import BaseModel, ConfigDict, Field

class User(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    # > allows object to be instantiated by field name or alias
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, str_to_lower=True, extra='forbid', populate_by_name=True)

    # > properties
    # > user_id must be greater than 0
    user_id: int = Field(alias="userId", gt=0)
    # > could use EmailStr pydantic type instead
    email_address: str = Field(pattern=r"^[\w,-]+@[a-zA-Z].{2,}$", alias="emailAddress")