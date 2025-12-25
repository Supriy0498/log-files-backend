from typing import List
from datetime import datetime

from schemas.log import Log, LogLevel, LogComponent
from type_defs.logs import LogList

def filter_logs_by_level(level: LogLevel, logs: LogList) -> LogList:
    return [log for log in logs if log.level == level]

def filter_logs_by_component(component: LogComponent, logs: LogList) -> LogList:
    return [log for log in logs if log.component == component]

def filter_logs_by_start_time(start_time: datetime, logs: LogList) -> LogList:
    return [log for log in logs if log.timestamp >= start_time]

def filter_logs_by_end_time(end_time: datetime, logs: LogList) -> LogList:
    return [log for log in logs if log.timestamp <= end_time]