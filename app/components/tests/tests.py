from typing import Annotated
from fastapi import APIRouter, Depends , File, UploadFile, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
import urllib.parse
import smtplib
from email.mime.text import MIMEText
from app.database import get_db_info
import os
from datetime import datetime, timedelta
from app.core.security import api_key_token
from app.core.config import settings
from app.scheduler.scheduler import scheduler
from apscheduler.triggers.date import DateTrigger

router = APIRouter(prefix="/test", tags=["tests"])
security = HTTPBearer(bearerFormat="test", scheme_name="JWT", description="JWT Token")

def myfunc(future_time):
    print(future_time)
    
@router.get("/", deprecated= True)
async def test():
    print(get_db_info())
    now = datetime.now()
    future_time = now + timedelta(seconds=30)
    job = scheduler.add_job(myfunc,trigger=DateTrigger(run_date=future_time),args=[future_time])
    return [{"test":settings.DATABASE_URL}]

@router.get("/remove_all_jobs" , deprecated= True)
async def get_url():
    scheduler.remove_all_jobs()
    return ["remove all job"]

@router.post("/Check_Authentication")
async def Check_Authentication(api_key : api_key_token):
    return ["Verified!"]

@router.get("/Get_Root_Key")
async def get_Root_Key():
    return [settings.ROOT_KEY]

@router.post("/send_test_email", deprecated= True)
async def send_test_email(email:str):
    return [{"send to": email}]