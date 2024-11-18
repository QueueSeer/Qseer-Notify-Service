from typing import Annotated
from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from app.database import get_db_info
import os

from app.core.config import settings

router = APIRouter(prefix="/test", tags=["tests"])
security = HTTPBearer(bearerFormat="test", scheme_name="JWT", description="JWT Token")


@router.get("/")
async def test():
    print(get_db_info())
    
    return [{"test": get_db_info()}]

#@router.post("/upload",deprecated=not settings.DEVELOPMENT)
#async def upload_file(file: UploadFile = File(...)):
    #if settings.DEVELOPMENT == False :
    #    raise HTTPException(status_code=503, detail='only available on dev server')
    
    #try:
        #get_s3_connect().upload_fileobj(file.file, get_s3_main_Bucket(), file.filename)
    #except Exception:
    #    raise HTTPException(status_code=500, detail='Something went wrong')
    #custom_url = "https://storage.qseer.app/"
    #return [{"filename": file.filename},{"fileType":file.content_type},{"url": custom_url + urllib.parse.quote(file.filename)}]

@router.get("/get_url",deprecated=not settings.DEVELOPMENT)
async def get_url(file_name:str):
    if settings.DEVELOPMENT == False :
        raise HTTPException(status_code=503, detail='only available on dev server')
    custom_url = "https://storage.qseer.app/"
    return [{"url": custom_url + urllib.parse.quote(file_name)}]

@router.post("/send_test_email",deprecated=not settings.DEVELOPMENT)
async def send_test_email(email:str):
    if settings.DEVELOPMENT == False :
        raise HTTPException(status_code=503, detail='only available on dev server')
    text = """\
    Hi,
    email from Qseer-Notify-Service
    """
    # Create MIMEText object
    receiver_email = email
    message = MIMEText(text, "plain")
    message["Subject"] = "No-reply"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Send the email
    with smtplib.SMTP(settings.smtp_SERVER, settings.smtp_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(settings.smtp_LOGIN, settings.smtp_PASSWORD)
        server.sendmail(settings.smtp_SENDER_NOREPLY_EMAIL, receiver_email, message.as_string())
    return [{"send to": email}]