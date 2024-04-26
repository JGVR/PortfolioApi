from typing import List
from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from .company import Company

class Experience(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id: int = Field(gt=0, alias="personId")
    job_title: str = Field(max_length=50, alias="jobTitle")
    job_description: str = Field(max_length=1000, default="", alias="jobDescription")
    company: Company = Field(max_length=100, alias="companyName")
    start_date: date = Field(alias="startDate", default=None)
    end_date: date = Field(alias="endDate", default=None)
    project_ids: List[int] = Field(alias="projectsId")