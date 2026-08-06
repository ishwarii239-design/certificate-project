from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.certificate import CertificateCreate, CertificateResponse
from app.services.certificate_service import create_certificate, get_certificate_by_id, get_all_certificates
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=CertificateResponse)
def create_cert(data: CertificateCreate, db: Session = Depends(get_db)):
    return create_certificate(db, data)

@router.get("/list", response_model=List[CertificateResponse])
def list_certs(db: Session = Depends(get_db)):
    return get_all_certificates(db)

@router.get("/{cert_id}", response_model=CertificateResponse)
def get_cert(cert_id: str, db: Session = Depends(get_db)):
    cert = get_certificate_by_id(db, cert_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert