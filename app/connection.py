import app.models as models
from app.database import engine,SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()