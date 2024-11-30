from app.scheduler.scheduler import scheduler
from apscheduler.triggers.date import DateTrigger
import requests
from datetime import datetime, timedelta
import json

def request_post(url,obj):
    x = requests.post(url, json = obj)
    print(x.text)

def schedule_date_post(url:str,obj:json,time_date:datetime):
    scheduler.add_job(request_post,trigger=DateTrigger(run_date=time_date),args=[url,obj])

def schedule_timedelta_post(url:str,obj:json,time_delta:timedelta):
    now = datetime.now()
    future_time = now + time_delta
    scheduler.add_job(request_post,trigger=DateTrigger(run_date=future_time),args=[url,obj])