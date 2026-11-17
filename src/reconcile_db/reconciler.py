from .model import Database, DatabaseStatus

class Reconciler():

    database: Database

    def __init__(self, provider: str, size: int, compute: str, status: DatabaseStatus) -> None:
        self.database = {
            "provider": provider,
            "size": size,
            "compute": compute,
            "status": status,
        }

    def is_database_running(self) -> bool:
        return self.database["status"] == DatabaseStatus.RUNNING
