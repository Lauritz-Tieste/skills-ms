from pydantic import BaseModel, Field

from api.schemas.skill import RootSkill, SubSkill
from api.schemas.skill_course import SkillCourse


class SearchResults(BaseModel):
    root_skills: list[RootSkill] = Field(description="List of root skills")
    sub_skills: list[SubSkill] = Field(description="List of sub skills")
    courses: list[SkillCourse] = Field(description="List of courses")
