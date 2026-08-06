from fastapi import APIRouter
from app.api.routes import certificate

api_router = APIRouter()

api_router.include_router(certificate.router, prefix="/certificate", tags=["Certificate"])
api_router.include_router(certificate.router, prefix="/api/certificates", tags=["Certificate"])