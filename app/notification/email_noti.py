from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings