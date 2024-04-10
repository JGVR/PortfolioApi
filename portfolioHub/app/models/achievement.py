from dataclasses import dataclass
from degree import Degree
from certificate import Certificate

@dataclass(frozen=True)
class Achievement:
    id: int
    certificate: Certificate
    degree: Degree