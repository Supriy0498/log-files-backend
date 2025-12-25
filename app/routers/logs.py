from fastapi import APIRouter, Request
from datetime import datetime
from typing import List, Optional

from schemas.log import Log, LogLevel, LogComponent
import services.logs as logs_service

logs_router = APIRouter()

@logs_router.get("/logs")
def get_logs() -> List[Log]:
    return logs_service.get_logs()