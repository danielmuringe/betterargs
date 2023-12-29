"""Create command line interfaces fast and easy"""


# Second party imports
from .constructor import construct
from .deserializer import deserialize
from .utils import Any, PathLike, read_file


def construct_from_dict(tree: dict[str, Any]) -> dict[str, Any]:
    """Construct a dict from a dict with a tree structure

    Args:
        tree (dict[str, Any]): A dict with an arguments tree structure

    Returns:
        dict[str, Any]: The arguments expected
    """
    return construct(tree)


def construct_from_string(tree: str, serial_format: str) -> dict[str, Any]:
    """Construct a dict from a string with a tree structure

    Args:
        tree (str): A string with an arguments tree structure in a certain serialization format

    Returns:
        dict[str, Any]: The arguments expected
    """

    tree_dict = deserialize(tree, serial_format)
    return construct_from_dict(tree_dict)


def construct_from_file(tree_path: PathLike, serial_format: str) -> dict[str, Any]:
    """Construct a dict from a file with a tree structure

    Args:
        tree_path (str): A path to a file with an arguments tree structure in a certain serialization format
        encoding (str, optional): The encoding of the file. Defaults to "utf-8".

    Returns:
        dict[str, Any]: The arguments expected
    """

    tree_str = read_file(tree_path)
    return construct_from_string(tree_str, serial_format)
