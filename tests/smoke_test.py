from reconcile_db import Reconcile

def test_smoke() -> None:
    """
    A simple smoke test to ensure that service is working correctly.
    """
    reconcile = Reconcile(provider="PostgreSql", size=10, compute="medium", status="RUNNING")
    assert reconcile.IsDatabaseRunning() is True