from dataclasses import dataclass
from school import School

@dataclass(frozen=True)
class Degree:
    name: str
    type: str
    description: str
    school: School