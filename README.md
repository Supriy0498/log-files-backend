# Log Analysis REST API

## Tech Stack - Python, FastAPI, Pydantic

## Assumptions Made
* Logs are stored in `logs/` folder & have file type of `.log`
* The log directory size fits within the system's available RAM
* Reading & parsing log files at server startup, so any logs added after wont be reflected unless server restarts.
* Unique log ids (uuid) are assigned during each parsing step. If server restarts, new ids will assigned to same log lines


## Further Improvements
* Implementation of something like File Watcher for listening log file changes & updating logs
* Pagination for large logs handling
* Transition from In memory log parsing/storing to Database(PostgreSQL, etc)
