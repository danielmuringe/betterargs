""""Deserializer for betterargs"""

# Built-in imports
from json import loads as json_deserialize

# PIP imports
from toml import loads as toml_deserialize
from xmltodict import parse as xml_deserialize
from yaml import safe_load as yaml_deserialize

# Second-party imports
from .utils import Any


def deserialize(serialized_str: str, serial_format: str) -> dict[str, Any]:
    """Deserialize a string into a dict

    Args:
        serialized_str (str): The string to deserialize

    Returns:
        dict[str, Any]: Deserialized objects in python dict form
    """

    return {}
