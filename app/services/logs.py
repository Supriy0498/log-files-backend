from typing import List

from utils import logs_parser
from schemas.log import Log

_logs = []

def parse_logs_on_startup(directory: str):
    global _logs
    _logs = logs_parser.parse_logs(directory)

def get_logs() -> List[Log]:
    return _logs