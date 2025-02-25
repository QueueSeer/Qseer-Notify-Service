from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import get_db_info
from app.authentication.api_key import create , verify 
from app.core.config import settings
from app.core.security import api_key_token
from app.email.email_service import send_email
from app.authentication.api_key import verify_root_key
from typing import Annotated
import logging

from app.database.connection import async_session

from sqlalchemy import delete, select, update, insert
from app.database.models import User , Appointment , ApmtStatus


from app.scheduler.scheduler import scheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta

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

class AppointmentEmail(BaseModel):
    appointment_ID : int = Field( examples=[42069])
    time_date : datetime


@router.post("/send_verify_email")
async def send_verify_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    if send_email("Verify Your Email Address","Hello!","",'''
                Thank you for signing up with Qseer! Please verify your email address to complete the registration process. Click the button below to verify your email
               ''',"Verify Email Address",url,email) :
        return [{"send to": email}]
    else:
        raise HTTPException(status_code=503, detail="Fail to Send Email")

@router.post("/send_verify_seer_email")
async def send_verify_seer_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    if send_email("Verify Your Email Address","Hello!","",'''
                Thank you for signing up with Qseer! Please verify your email address to complete the registration process. Click the button below to verify your email
               ''',"Verify Email Address",url,email) :
        return [{"send to": email}]
    else:
        raise HTTPException(status_code=503, detail="Fail to Send Email")

@router.post("/send_change_password_email")
async def send_change_password_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    if send_email("Reset Your Password","Hi!","",'''
                We received a request to reset the password for your Qseer account. If you made this request, please click the button below to set a new password
               ''',"Reset Password",url,email):
        return [{"send to": email}]
    else:
        raise HTTPException(status_code=503, detail="Fail to Send Email")

@router.post("/send_change_email_email")
async def send_change_email_email(api_key : api_key_token,urlEmail : UrlEmail):
    url = urlEmail.url
    email = urlEmail.email
    if send_email("Confirm Email Change Request","Hello!","",'''
                We received a request to update the email address associated with your Qseer account. To confirm this change, please click the button below
               ''',"Confirm Email Change",url,email) :
        return [{"send to": email}]
    else:
        raise HTTPException(status_code=503, detail="Fail to Send Email")
    

logger = logging.getLogger('uvicorn.error')

async def trigger_send_appointment_email(appointment_ID : int):
    stmt = (
        select(Appointment).
        where(Appointment.id == appointment_ID)
    )
    async with async_session() as session:
        appointment_info = (await session.scalars(stmt)).one_or_none()
        if appointment_info is None:
            logger.warning(f"Not Found Appointment_info")
            return
        if appointment_info.status == ApmtStatus.pending :
            stmt_2 = (
                select(User).
                where(User.id == appointment_info.client_id)
            )
            user_info = (await session.scalars(stmt_2)).one()
            user_email = user_info.email
            send_email("Reminder: Upcoming Appointment Confirmation","Hello!","",'''
                your appointment is coming up soon
               ''',"Qseer","qseer.app",user_email)
            logger.info(f"Send to Email : {user_email}")
        else:
            logger.warning(f"ApmtStatus Not pending")

@router.post("/send_appointment_email") 
async def send_appointment_email(api_key : api_key_token , appEmail : AppointmentEmail):
    future_time = appEmail.time_date + timedelta(seconds=60)
    scheduler.add_job(trigger_send_appointment_email,trigger=DateTrigger(run_date=future_time),args=[appEmail.appointment_ID])
    return ["add to scheduler complete"]