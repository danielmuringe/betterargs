"""All package tests"""


# PIP installed imports
from pytest import mark, MonkeyPatch, raises

# Second party imports
from betterargs.utils import Path


# Constants
TEST_DIR = Path(__file__).parent
TEST_DATA_PATH = TEST_DIR / "data"
