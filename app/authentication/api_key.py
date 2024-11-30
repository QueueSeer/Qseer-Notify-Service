import psycopg
from app.database import get_db_info 
import secrets
import string
from app.core.config import settings

def verify(api_key:str):
    query = "SELECT EXISTS(SELECT 1 FROM app_api_key WHERE api_key = %s)"
    exists = None
    try:
        with psycopg.connect(get_db_info()) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (api_key,))
                exists = cur.fetchone()[0]
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    if exists:
        return True
    else:
        return False

def verify_root_key(key):
    if key == settings.ROOT_KEY:
        return True
    else:
        return False

def create():
    def generate_api_key(length=64):
        characters = string.ascii_letters + string.digits  
        return ''.join(secrets.choice(characters) for _ in range(length))
    
    def insert_api_key_to_db(api_key):
        query = "INSERT INTO app_api_key (api_key) VALUES (%s);"  # Adjust if needed
        try:
            with psycopg.connect(get_db_info()) as conn:
                with conn.cursor() as cur:
                    cur.execute(query, (api_key,))
                    conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"An error occurred: {e}")

    current_key = generate_api_key()
    insert_api_key_to_db(current_key)
    return current_key