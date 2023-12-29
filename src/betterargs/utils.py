"""Common objects and package utilities"""


# Built-in imports
from os import PathLike
from pathlib import Path
from typing import Any, Callable


# Constants
BASE_DIR = Path(__file__).parent
ENC = "utf-8"
SERIALIZATION_FORMATS = [
    "json",
    "yaml",
    "toml",
    "xml",
]


def read_file(path: PathLike) -> str:
    """Read a text file and return its contents as string"""
    with open(path, encoding=ENC, mode="r") as f:
        return f.read()
