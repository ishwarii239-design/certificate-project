from pydantic import BaseModel
from typing import Optional

class CertificateCreate(BaseModel):
    student_name: str
    course_name: str
    issue_date: str
    email: Optional[str] = None
    certificate_id: Optional[str] = None
    template_num: Optional[int] = 10
    certificate_html: Optional[str] = None

class CertificateResponse(BaseModel):
    id: int
    student_name: str
    course_name: str
    issue_date: str
    email: Optional[str] = None
    certificate_id: str
    template_num: Optional[int] = 10
    certificate_html: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True