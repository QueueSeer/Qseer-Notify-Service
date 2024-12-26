from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings
from app.core.security import api_key_token
from app.email.email_service import send_email
from app.authentication.api_key import verify_root_key
from typing import Annotated

from fastapi import Body
from pydantic import BaseModel, Field

router = APIRouter(prefix="/email", tags=["email"])

class GenericEmail(BaseModel):
    email: str = Field(min_length=3, examples=["no-reply@qseer.app"])
    header:str = Field(min_length=3, examples=["Verify Your Email Address"])
    body_header1:str = Field(min_length=3, examples=["Hello"])
    body_header2:str = Field(min_length=3, examples=["Thank you for signing up with Qseer!"])
    body:str = Field(min_length=3, examples=["Please verify your email address to complete the registration process.Click the button below to verify your email"])
    button_text:str = Field(min_length=3, examples=["Verify Email Address"])
    button_link:str = Field(min_length=3, examples=["backend.qseer.app/Nice"])

@router.post("/send_generic_email")
async def send_generic_email(api_key : api_key_token,genericEmail :GenericEmail):
    header = genericEmail.header
    body_header1 = genericEmail.body_header1
    body_header2 = genericEmail.body_header2
    body = genericEmail.body
    button_text = genericEmail.button_text
    button_link = genericEmail.button_link
    email = genericEmail.email
    send_email(header,body_header1,body_header2,body,button_text,button_link,email)
    return [{"send to": email}]


class UrlEmail(BaseModel):
    url: str = Field(min_length=3, examples=["backend.qseer.app"])
    email: str = Field(min_length=3, examples=["no-reply@qseer.app"])


@router.post("/send_verify_email")
async def send_verify_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    send_email("Verify Your Email Address","Hello!","",'''
                Thank you for signing up with Qseer! Please verify your email address to complete the registration process. Click the button below to verify your email
               ''',"Verify Email Address",url,email)
    return [{"send to": email}]

@router.post("/send_verify_seer_email")
async def send_verify_seer_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    send_email("Verify Your Email Address","Hello!","",'''
                Thank you for signing up with Qseer! Please verify your email address to complete the registration process. Click the button below to verify your email
               ''',"Verify Email Address",url,email)
    return [{"send to": email}]

@router.post("/send_change_password_email")
async def send_change_password_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    send_email("Reset Your Password","Hi!","",'''
                We received a request to reset the password for your Qseer account. If you made this request, please click the button below to set a new password
               ''',"Reset Password",url,email)
    return [{"send to": email}]

@router.post("/send_change_email_email")
async def send_change_email_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    send_email("Confirm Email Change Request","Hello!","",'''
                We received a request to update the email address associated with your Qseer account. To confirm this change, please click the button below
               ''',"Confirm Email Change",url,email)
    return [{"send to": email}]