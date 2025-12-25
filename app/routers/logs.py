from fastapi import APIRouter
from datetime import datetime
from typing import List, Optional

from schemas.log import Log, LogLevel, LogComponent
import services.logs as logs_service
from type_defs.logs import LogList

logs_router = APIRouter()

@logs_router.get("/logs")
def get_logs(
    level: Optional[LogLevel] = None, 
    component: Optional[LogComponent] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
) -> LogList:
    return logs_service.get_logs(level, component, start_time, end_time)

@logs_router.get("/logs/stats")
def get_logs_stats():
    return logs_service.get_logs_stats()

@logs_router.get("/logs/{log_id}")
def get_log(log_id: str) -> Log:
    return logs_service.get_log(log_id)