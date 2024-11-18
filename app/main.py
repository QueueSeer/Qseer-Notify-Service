from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.components import get_api_router
from app import (
    start_up
#    objectStorage
)

lock_file = "app/startup_task.lock"
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # database.create_tables()
    if not os.path.exists(lock_file):
        try:
            # Create the lock file
            with open(lock_file, "w") as f:
                f.write("lock")

            print("Running startup task...")
            start_up.run_start_up_script()
        except Exception as e:
            print(f"Error during startup task: {e}")
        finally:
            print("Startup task completed.")
    else:
        print("Startup task already completed by another worker.")
    yield
    if os.path.exists(lock_file):
        try:
            os.remove(lock_file)
            print("Lock file removed.")
        except Exception as e:
            print(f"Error removing lock file: {e}")
    # shutdown


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(get_api_router())


@app.get("/", response_class=HTMLResponse)
async def root():
    #return FileResponse('static/index.html')
#app.mount('/',StaticFiles(directory='static', html=True), name='static')
    return '''\
<style>
    a {
        margin: 1em;
        padding: 1em;
        border: 2px solid #333333;
        border-radius: 0.5em;
        text-decoration: none;
        color: black;
        background-color: white;
        transition: 0.2s;
    }

    a:hover {
        background-color: #f0f0f0;
    }

    a:active {
        background-color: #f0f0f0;
        transform: scale(0.98);
    }
</style>
<div style='display: flex; flex-direction: column; align-items: center;'>
    <h1>Documentations</h1><br>
    <a href='./docs'>Interactive API docs</a>
    <a href='./redoc'>Alternative API docs</a>
</div>
'''