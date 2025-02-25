from app.core.config import settings

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor ,ProcessPoolExecutor

# Database configuration
DB_URL = settings.DATABASE_URL

# Configure APScheduler
scheduler = AsyncIOScheduler(
    jobstores={
        'default': SQLAlchemyJobStore(url=DB_URL)
    },
    executors={
        'processpool': ProcessPoolExecutor(max_workers=5)
    },
    job_defaults={
        'coalesce': False,
        'max_instances': 3
    }
)
print("Hello from scheduler")