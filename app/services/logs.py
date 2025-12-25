from typing import List, Optional
from datetime import datetime
from fastapi import HTTPException, status

from utils import logs_parser, logs_filter
from schemas.log import Log, LogLevel, LogComponent
from type_defs.logs import LogDict, LogList

_logs: LogDict = {}

def parse_logs_on_startup(directory: str):
    global _logs
    _logs = logs_parser.parse_logs(directory)

def get_logs(level: Optional[LogLevel] = None, 
    component: Optional[LogComponent] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None
) -> LogList:
    
    filtered_logs = _logs.values()
    if level is not None:
        filtered_logs = logs_filter.filter_logs_by_level(level, filtered_logs)

    if component is not None:
        filtered_logs = logs_filter.filter_logs_by_component(component, filtered_logs)
    
    if start_time is not None:
        filtered_logs = logs_filter.filter_logs_by_start_time(start_time, filtered_logs)

    if end_time is not None:
        filtered_logs = logs_filter.filter_logs_by_end_time(end_time, filtered_logs)
        
    return filtered_logs


def get_logs_stats():
    total_logs = len(_logs)
    log_count_per_level = dict()
    for level in LogLevel:
        log_count_per_level[level.name] = 0

    log_count_per_component = dict()
    for component in LogComponent:
        log_count_per_component[component.name] = 0

    for log in _logs.values():
        log_count_per_level[log.level.name]+=1
        log_count_per_component[log.component.name]+=1

    return {
        "total_logs": total_logs,
        "log_count_per_level": log_count_per_level,
        "log_count_per_component": log_count_per_component
    }

def get_log(log_id) -> Log:
    log = _logs.get(log_id, None)
    if log is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log with id '{}' not found!".format(log_id))

    return log