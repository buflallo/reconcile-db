from .model import Database, DatabaseStatus

class Reconcile:

    database: Database

    def __init__(self, provider, size, compute, status):
        self.database = {
            "provider": "PostgreSql",
            "size": 10,
            "compute": "medium",
            "status": DatabaseStatus.RUNNING,
        }

    def IsDatabaseRunning(self) -> bool:
        return self.database["status"] == DatabaseStatus.RUNNING
