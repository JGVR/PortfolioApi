from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import datetime
from .company import Company
from ..services.reference_integrity_checker import ReferenceIntegrityChecker

class Experience(BaseModel):
    # > make fields immutable after instantiation.
    # > strip white spaces from all str fields
    # > rejects extra fields from been added
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True, extra='forbid')

    id: int = Field(gt=0, alias="_id")
    person_id: int = Field(gt=0, alias="personId")
    project_ids: List[int] = Field(alias="projectIds", default=[])
    job_title: str = Field(max_length=50, alias="jobTitle")
    job_description: str = Field(max_length=1000, default="", alias="jobDescription")
    company: Company
    start_date: Optional[datetime] = Field(alias="startDate", default=None)
    end_date: Optional[datetime] = Field(alias="endDate", default=None)

    @field_validator('person_id', mode="before")
    def check_person_id(cls, id) -> int:
        exists = ReferenceIntegrityChecker.check_id_existence("portfolio", "persons",id)
        if exists == False:
            raise ValueError(f"The person Id: {id} was not found in the persons collection. Please make sure the person exists before assigning an experience to a person.")
        return id
    
    
    @field_validator('project_ids', mode="before")
    def check_project_ids(cls, ids) -> List[int]:
        results = [ReferenceIntegrityChecker.check_id_existence("portfolio", "projects",id) for id in ids]
        if all(results) == False:
            raise ValueError(f"There is one or more project ids that were not found in the projects collection. Please make sure the projects exists before assigning a project to an experience.")
        return ids