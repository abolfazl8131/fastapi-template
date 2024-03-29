
import app.schemas as schemas
from app.config.settings import app
from app.services import wellcome_service
from app.config.connection import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

@app.get("/")
def wellcome_api(db:Session = Depends(get_db)):
    
    return wellcome_service()
    
