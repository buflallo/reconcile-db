from reconcile_db import Reconciler, DatabaseStatus

def test_smoke() -> None:
    """
    A simple smoke test to ensure that service is working correctly.
    """
    reconciler = Reconciler(provider="PostgreSql", size=10, compute="medium", status=DatabaseStatus.RUNNING)
    assert reconciler.is_database_running() is True