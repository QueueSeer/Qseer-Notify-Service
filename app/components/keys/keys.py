from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings

router = APIRouter(prefix="/keys", tags=["keys"])

@router.get("/")
async def test():
    return [{"test":":3"}]

@router.post("/create")
async def createKey(root_key:str):
    if root_key != settings.ROOT_KEY or settings.OPEN_KEY_GEN == False :
        return [{"api_key":"Nice Try Rocket"}]
    return [{"api_key :":create()}]