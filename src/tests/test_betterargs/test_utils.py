"""Test the utils module in betterargs"""


# Second-party imports
from betterargs.utils import BASE_DIR, ENC, SERIALIZATION_FORMATS, read_file
from .. import TEST_DATA_PATH, raises


def test_constants():
    """Test constants"""

    # Base directory
    assert BASE_DIR.name == "betterargs"
    assert BASE_DIR.parent.name == "src"

    # Encoding
    assert ENC == "utf-8"

    # Serialization formats
    assert SERIALIZATION_FORMATS == [
        "json",
        "yaml",
        "toml",
        "xml",
    ]


def test_read_file():
    """Test read_file function"""

    FILE_TO_BE_READ_PATH = TEST_DATA_PATH / "files_to_be_read"

    # Test read_file with utf-8 encoded file
    assert (
        read_file(FILE_TO_BE_READ_PATH / "utf-8.txt")
        == "Just random text\nin a file with utf-8 encoding\nfor a test\n"
    )

    # Test read_file with non-utf-8 encoded file
    assert (
        read_file(FILE_TO_BE_READ_PATH / "non-utf-8.txt")
        == "Just random text\nin non utf-8 file\nfor a test\n"
    )

    # Test non-existent file
    with raises(FileNotFoundError) as file_not_found_error:
        read_file(TEST_DATA_PATH / "files_to_be_read/non-existent.txt")
    assert file_not_found_error.value.args[1] == "No such file or directory"
