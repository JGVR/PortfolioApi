from typing import List
from dataclasses import dataclass
from skill import Skill

@dataclass(frozen=True)
class Project:
    id: int
    name: str
    description: str
    skills: List[Skill]
    images: List[str]
    url: str