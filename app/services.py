import app.schemas
import validators
from app.exceptions import raise_bad_request

# here develop services

def wellcome_service():
    return {
        'message':"wellcome"
    }