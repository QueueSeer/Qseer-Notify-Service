from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings
from app.core.security import api_key_token

router = APIRouter(prefix="/keys", tags=["keys"])

@router.get("/", deprecated= True)
async def test():
    return [{"test":":3"}]

@router.post("/create")
async def createKey(root_key:api_key_token):
    return [{"api_key :":create()}]