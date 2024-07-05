import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import app_config_main, app_config_host, app_config_port, app_config_reload
from app.database import sql_database_connection
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/healthz")
async def healthz():
    return {"status": "healthy"}


def start():
    uvicorn.run(app_config_main, host=app_config_host, port=int(app_config_port), reload=app_config_reload)
