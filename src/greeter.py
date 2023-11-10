"""Module providing basic greeting print function."""


class Greeter:
    """A friendly greeter who says hi"""

    def __init__(self) -> None:
        self.guests = []

    def greet(self, name):
        """Says hello, given a name"""
        print(f"Hello, {name}!")
        self.guests.append(name)

    def bye(self, name):
        """Says goodbye, given a name"""
        print(f"Byebye, {name}!")
