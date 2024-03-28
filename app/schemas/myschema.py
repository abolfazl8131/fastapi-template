# shortener_app/schemas.py
from pydantic import BaseModel


class Wellcome(BaseModel):
    msg:int
    user:str