"""A simple example used to show off linter"""
from typing import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
