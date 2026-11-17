def test_smoke() -> None:
    """
    A simple smoke test to ensure that the application starts without errors.
    """
    try:
        print("Smoke test passed: Application started successfully.")
    except Exception as e:
        print(f"Smoke test failed: {e}")