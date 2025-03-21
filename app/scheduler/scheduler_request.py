from app.scheduler.scheduler import scheduler
from apscheduler.triggers.date import DateTrigger
import requests
import httpx
from datetime import datetime, timedelta
import json

import logging

logger = logging.getLogger('uvicorn.error')
logger.info("received Trigger Request")

async def request_post(url,obj):
    logger.info("Send_auction_trigger")
    # x = requests.post(url, json = obj)
    # logger.info(x.text)
    logger.info(obj)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                url,
                json=obj,
                timeout=30
            )
            success = response.is_success
        except httpx.TimeoutException:
            success = False
    if not success:
        logger.warning(f"Failed to send Trigger Noti")
        logger.warning(f"Url: {url}")
    logger.info(f"Send Trigger Complete")

def schedule_date_post(url:str,obj,time_date:datetime):
    scheduler.add_job(request_post,trigger=DateTrigger(run_date=time_date),args=[url,obj])

def schedule_timedelta_post(url:str,obj:json,time_delta:timedelta):
    now = datetime.now()
    future_time = now + time_delta
    scheduler.add_job(request_post,trigger=DateTrigger(run_date=future_time),args=[url,obj])