"""Basic runner / main entrypoint file"""

from greeter import Greeter

if __name__ == "__main__":
    greeter = Greeter()
    greeter.greet("John")
