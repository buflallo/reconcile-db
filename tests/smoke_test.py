from reconcile_db import Reconciler, DatabaseStatus

def test_green() -> None:
    """
    Test that the Reconciler correctly identifies a running/stoppped database status.
    """
    reconciler = Reconciler(provider="PostgreSql", size=10, compute="medium", status=DatabaseStatus.RUNNING)
    assert reconciler.is_database_running() is True
    reconciler.database["status"] = DatabaseStatus.STOPPED
    assert reconciler.is_database_running() is False

def test_red() -> None:
    """
    Test that the Reconciler correctly identifies a bug in the running/stoppped status.
    """
    reconciler = Reconciler(provider="PostgreSql", size=10, compute="medium", status=DatabaseStatus.STOPPED)
    assert reconciler.is_database_running() is False
    reconciler.database["status"] = DatabaseStatus.RUNNING
    assert reconciler.is_database_running() is True