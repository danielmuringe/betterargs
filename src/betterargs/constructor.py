"""Construct arguments tree to ArgumentParser arguments"""


# Built-in imports
from argparse import ArgumentParser


# Second-party imports
from .utils import Any


def construct(tree: dict[str, Any]) -> dict[str, Any]:
    """Construct arguments tree to ArgumentParser arguments"""

    return {}
