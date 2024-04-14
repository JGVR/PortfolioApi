from typing import List
from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from company import Company

class Job(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=50, max_length=500)
    company: Company 
    start_date: date
    end_date: date
    project_ids: List[int] = Field(default=[])