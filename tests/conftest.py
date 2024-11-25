import pytest
import psutil


@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests():
    yield
    # Ensure all child processes are terminated
    current_process = psutil.Process()
    for child in current_process.children(recursive=True):
        child.terminate()
        child.wait()
