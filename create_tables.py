from app.core.database import engine, Base
from app.models import certificate

Base.metadata.create_all(bind=engine)