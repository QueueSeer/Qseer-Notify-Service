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

from app.scheduler.scheduler_request import schedule_date_post

from sqlalchemy import delete, select, update, insert
from app.database.models import User , Appointment , ApmtStatus


from app.scheduler.scheduler import scheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta

from fastapi import Body
from pydantic import BaseModel, Field
import json

MAIN_BACKEND_URL = settings.MAIN_BACKEND_HOST
protocal = "http://"

logger = logging.getLogger('uvicorn.error')

router = APIRouter(prefix="/trigger", tags=["trigger"])

class Auction_Trigger_Info(BaseModel):
    auction_ID : int = Field( examples=[42069])
    time_date : datetime
    trigger_url_part : str = Field(examples=["/auction/proc"])
    security_key : str = Field(examples=["JHAKHSD*********"])

@router.post("/auction")
async def auction_trigger(api_key : api_key_token,auction_trigger_info : Auction_Trigger_Info):
    logger.info("received Trigger Request")
    obj = {
        'auction_ID' : auction_trigger_info.auction_ID,
        'time_date' : auction_trigger_info.time_date.isoformat(),
        'security_key' : auction_trigger_info.security_key
    }
    schedule_date_post(
        protocal+MAIN_BACKEND_URL+auction_trigger_info.trigger_url_part,
        obj,
        auction_trigger_info.time_date
    )
    return ["received Trigger Request"]