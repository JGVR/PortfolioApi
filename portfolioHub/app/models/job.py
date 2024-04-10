from typing import List
from dataclasses import dataclass
from datetime import date
from company import Company

@dataclass(frozen=True)
class Job:
    id: int
    title: str
    description: str
    company: Company 
    start_date: date
    end_date: date
    project_ids: List[int]