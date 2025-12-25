from fastapi import FastAPI
from pathlib import Path

from routers.logs import logs_router
from services.logs import parse_logs_on_startup

async def lifespan(app: FastAPI):
    logs_directory = Path(__file__).resolve().parent.parent / "logs"
    parse_logs_on_startup(logs_directory)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(logs_router)