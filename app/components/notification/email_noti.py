from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from app.email.email_service import send_email
from app.authentication.api_key import verify_root_key

router = APIRouter(prefix="/email", tags=["email"])

@router.post("/send_generic_email")
async def send_generic_email(backend_verify_key:str,header:str,body_header1:str,body_header2:str,body:str,button_text:str,button_link:str,email:str):
    if not verify_root_key(backend_verify_key) :
        raise HTTPException(status_code=401, detail="Unauthorized")
    send_email(header,body_header1,body_header2,body,button_text,button_link,email)
    return [{"send to": email}]

@router.post("/send_verify_email")
async def send_verify_email(backend_verify_key:str,url:str,email:str):
    if not verify_root_key(backend_verify_key) :
        raise HTTPException(status_code=401, detail="Unauthorized")

    send_email("Verify Your Email Address","Hello!","",'''
                Thank you for signing up with Qseer! Please verify your email address to complete the registration process.Click the button below to verify your email
               ''',"Verify Email Address",url,email)
    return [{"send to": email}]