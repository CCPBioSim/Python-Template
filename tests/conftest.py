import os
import shutil
import tempfile

import pytest


@pytest.fixture
def temp_test_dir():
    """
    Provides a temporary test directory with a 'logs' subfolder.
    Automatically cleans up after the test.
    """
    test_dir = tempfile.mkdtemp(prefix="example_package_YOUR_USERNAME_HERE_")
    logs_path = os.path.join(test_dir, "logs")
    os.makedirs(logs_path, exist_ok=True)

    orig_dir = os.getcwd()
    os.chdir(test_dir)

    yield test_dir, logs_path  # make available to tests

    os.chdir(orig_dir)
    shutil.rmtree(test_dir, ignore_errors=True)
