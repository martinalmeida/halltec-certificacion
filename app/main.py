from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes.router import example_router

load_dotenv()

app = FastAPI()

app.include_router(example_router)

@app.get("/config")
def read_config():
    app_name = os.getenv("APP_NAME", "Default App")
    app_env = os.getenv("APP_ENV", "production")
    return {"app_name": app_name, "environment": app_env}