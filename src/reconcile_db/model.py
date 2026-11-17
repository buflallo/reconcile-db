from typing import Literal, TypedDict
from enum import StrEnum

class DatabaseStatus(StrEnum):
    PROVISIONING = "provisioning"
    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"

class Database(TypedDict):
    provider: Literal["PostgreSql"]
    size: int
    compute: Literal["small", "medium", "high"]
    status: DatabaseStatus