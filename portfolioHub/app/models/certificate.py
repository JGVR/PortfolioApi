from .school import School
from .entity import Entity
from pydantic import Field

class Certificate(Entity):
    url: str = Field(default="")
    description: str = Field(max_length=150, default="")
    platform: School