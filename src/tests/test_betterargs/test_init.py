"""Test the __init__ file"""


# Second party imports
from betterargs import construct_from_file
from betterargs.utils import read_file, SERIALIZATION_FORMATS
from .. import TEST_DATA_PATH, MonkeyPatch, mark, raises


class TestConstructorFunctions:
    """Test the constructor functions"""

    CLI_INPUTS = [
        # Required argument missing
        (
            "test_cli_app init first_app",
            SystemExit,
        ),
        # No command passed
        (
            "test_cli_app -p /tmp",
            SystemExit,
        ),
        # Violating mutual exclusion
        (
            "test_cli_app -p /tmp -v",
            SystemExit,
        ),
        # Good definition of init command
        (
            "test_cli_app -p /tmp init first_app",
            {
                "path": "/tmp",
                "version": False,
                "command": "init",
                "name": "first_app",
                "quiet": False,
                "verbose": False,
            },
        ),
        # Good definition of init command with flag argument
        (
            "test_cli_app -p /tmp init first_app -q",
            {
                "path": "/tmp",
                "version": False,
                "command": "init",
                "name": "first_app",
                "quiet": True,
                "verbose": False,
            },
        ),
        # Violating of init command flag arguments mutual exclusion
        (
            "test_cli_app -p /tmp init first_app -q -v",
            SystemExit,
        ),
        # Defining two commands
        (
            "test_cli_app -p /tmp init first_app init purge first_app",
            SystemExit,
        ),
    ]

    @mark.parametrize("cli_input,expected", CLI_INPUTS)
    def test_constructor_functions_in_action(
        self, monkeypatch: MonkeyPatch, cli_input, expected
    ):
        """Test the Constructor functions in action"""

        for serialization_format in SERIALIZATION_FORMATS:
            monkeypatch.setattr("sys.argv", cli_input.split(" "))

            args_tree_path = TEST_DATA_PATH / f"args/args.{serialization_format}"

            if isinstance(expected, dict):
                args_from_cli = construct_from_file(
                    args_tree_path, serialization_format
                )
                assert args_from_cli == expected
            else:
                with raises(expected) as error:
                    assert construct_from_file(args_tree_path, serialization_format)
                assert error.type == expected
