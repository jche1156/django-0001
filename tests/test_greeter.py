import unittest
from unittest.mock import patch

from greeter import Greeter

class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_default_greeting_set(self, mock_print):
        greeter = Greeter()
        greeter.greet("world")
        mock_print.assert_called_with("Hello, world!")

    @patch('builtins.print')
    def test_greet(self, mock_print):
        # The actual test
        greeter = Greeter()
        greeter.greet('John')
        mock_print.assert_called_with("Hello, John!")
        greeter.greet('Eric')
        mock_print.assert_called_with("Hello, Eric!")

if __name__ == '__main__':
    unittest.main()