from app.core.config import settings

def get_db_info():
    PG_USERNAME = settings.PG_USERNAME
    PG_PASSWORD = settings.PG_PASSWORD
    PG_HOST = settings.PG_HOST
    PG_PORT = settings.PG_PORT
    PG_DATABASE = settings.PG_DATABASE
    return f"dbname={PG_DATABASE} user={PG_USERNAME} password={PG_PASSWORD} host={PG_HOST} port={PG_PORT}"
