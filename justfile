format_test_lint:
    black src tests
    pytest
    pylint src
    pylint --disable=E0401 tests

lint:
    pylint src
    pylint --disable=E0401 tests

watch:
    pytest -f

run:
    python src/main.py

code:
    code README.md src/main.py tests/test_django.py justfile

install:
    pip install -r requirements.txt

install_dev:
    pip install -r .devcontainer/requirements-dev.txt