from dataclasses import dataclass
from school import School
from entity import Entity

@dataclass(frozen=True)
class Certificate(Entity):
    name: str
    url: str
    description: str
    platform: School