from .model import Database, DatabaseStatus

class Reconciler():

    database: Database

    def __init__(self, provider: str, size: int, compute: str, status: DatabaseStatus) -> None:
        self.database = {
            "provider": "PostgreSql",
            "size": 10,
            "compute": "medium",
            "status": DatabaseStatus.RUNNING,
        }

    def is_database_running(self) -> bool:
        return self.database["status"] == DatabaseStatus.RUNNING
