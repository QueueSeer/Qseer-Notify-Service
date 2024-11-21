import psycopg
from app.database import get_db_info 
from app.scheduler.scheduler import scheduler

def run_start_up_script():
    try:

        with psycopg.connect(get_db_info()) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                        CREATE TABLE IF NOT EXISTS app_api_key (
                            api_key VARCHAR(64) NOT NULL,
                         PRIMARY KEY (api_key)
                        )
                    """)
                print("Table `app_api_key` ensured to exist.")
                #cur.execute(
                #"INSERT INTO app_api_key (api_key) VALUES (%s)",
                #"Don't add feature")
                cur.execute("SELECT * FROM app_api_key")
                cur.fetchone()
                for record in cur:
                    print(record)
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    print("Hello from start up script")
    scheduler.start()
    return 