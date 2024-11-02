from pydantic import BaseModel, Field

from api.schemas.skill import SubSkill


class SkillCourse(BaseModel):
    skill_id: str = Field(max_length=256, description="ID of the skill")
    skill: SubSkill = Field(description="ID of the skill")
    course_id: str = Field(max_length=256, description="ID of the course")
