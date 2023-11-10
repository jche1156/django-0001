"""Demonstrates basic unit testing and mocking"""

import unittest
from unittest.mock import patch

from greeter import Greeter


class GreeterTestSuite(unittest.TestCase):
    """Tests basic functionality of sample Greeter class"""

    @patch("builtins.print")
    def test_default_greeting(self, mock_print):
        """The classic hello world test, with mocked print function"""
        greeter = Greeter()
        greeter.greet("world")
        mock_print.assert_called_with("Hello, world!")

    @patch("builtins.print")
    def test_greet_by_name(self, mock_print):
        """Test that greeter takes names and changes accordingly"""
        greeter = Greeter()
        greeter.greet("John")
        mock_print.assert_called_with("Hello, John!")
        greeter.greet("Eric")
        mock_print.assert_called_with("Hello, Eric!")

    @patch("builtins.print")
    def test_goodbye(self, mock_print):
        """Test that greeter says bye as well"""
        greeter = Greeter()
        greeter.bye("John")
        mock_print.assert_called_with("Byebye, John!")
        greeter.bye("Eric")
        mock_print.assert_called_with("Byebye, Eric!")
        greeter.bye("George")
        mock_print.assert_called_with("Byebye, George!")


if __name__ == "__main__":
    unittest.main()
