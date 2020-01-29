"""Define common test utilities."""
import os

TEST_BAD_ZIP = "abcde"
TEST_ZIP = "00123"


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()
