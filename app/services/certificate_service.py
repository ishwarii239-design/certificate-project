import uuid
from app.models.certificate import Certificate

def generate_certificate_id():
    return "CERT-" + str(uuid.uuid4())[:8].upper()

def create_certificate(db, data):
    cert_id = data.certificate_id or generate_certificate_id()
    existing = db.query(Certificate).filter(Certificate.certificate_id == cert_id).first()
    
    if existing:
        existing.student_name = data.student_name
        existing.course_name = data.course_name
        existing.issue_date = data.issue_date
        existing.email = getattr(data, "email", None)
        existing.template_num = getattr(data, "template_num", 10)
        existing.certificate_html = getattr(data, "certificate_html", None)
        db.commit()
        db.refresh(existing)
        return existing
    else:
        new_cert = Certificate(
            student_name=data.student_name,
            course_name=data.course_name,
            issue_date=data.issue_date,
            email=getattr(data, "email", None),
            certificate_id=cert_id,
            template_num=getattr(data, "template_num", 10),
            certificate_html=getattr(data, "certificate_html", None)
        )
        db.add(new_cert)
        db.commit()
        db.refresh(new_cert)
        return new_cert

def get_certificate_by_id(db, cert_id: str):
    return db.query(Certificate).filter(Certificate.certificate_id == cert_id).first()

def get_all_certificates(db):
    return db.query(Certificate).order_by(Certificate.id.desc()).all()