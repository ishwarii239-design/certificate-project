from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    course_name = Column(String)
    issue_date = Column(String)
    template_num = Column(Integer, default=10, nullable=True)
    certificate_html = Column(Text, nullable=True)