from .school import School
from .entity import Entity
from pydantic import Field

class Degree(Entity):
    type: str = Field(min_length=15, max_length=50)
    description: str = Field(max_length=150, default="")
    school: School