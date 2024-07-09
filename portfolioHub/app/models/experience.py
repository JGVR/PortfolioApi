from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from .company import Company

class Experience(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    # > properties
    user_id: int = Field(gt=0, alias="userId")
    job_title: str = Field(max_length=100, alias="jobTitle")
    job_description: str = Field(max_length=1500, default="", alias="jobDescription")
    company: Company
    start_date: datetime = Field(alias="startDate", default=None)
    end_date: datetime = Field(alias="endDate", default=None)