"""Bare-bones Django-based test"""
from unittest import skip
from unittest.mock import patch

from django.test import TestCase
from greeter import Greeter


@skip("Django not set up yet")
class DjangoSmokeTestCase(TestCase):
    """A bare-minimum django test suite"""

    @patch("builtins.print")
    def test_django_greet(self, mock_print):
        """Test that greeter using a django test case"""
        greeter = Greeter()
        greeter.greet("John")
        mock_print.assert_called_with("Hello, John!")
