import os
import uuid
from datetime import datetime

from schemas.log import Log
from type_defs.logs import LogDict

def parse_logs(directory: str) -> LogDict:
    print("Parsing logs from directory", directory)
    if not os.path.exists(directory):
        print("Directory does not exist")
        return dict()
    
    logs = dict()
    for file_name in os.listdir(directory):
        if file_name.endswith(".log"):
            print("Reading log file named", file_name)
            with open(os.path.join(directory, file_name), 'r', encoding="utf-8") as file:
                next(file)
                for log_line in file:
                    log_values = log_line.rstrip("\n").split("\t")
                    if len(log_values) != 4:
                        print("Log line format incorrect")
                        continue

                    (timestamp, level, component, message) = log_values
                    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    log_id = str(uuid.uuid4())[:16]
                    log = Log(id=log_id, timestamp=timestamp, level=level, component=component, message=message)
                    logs[log_id] = log

    return logs