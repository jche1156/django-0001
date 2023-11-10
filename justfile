format_test_lint:
    black src tests
    pytest
    pylint src
    pylint --disable=E0401 tests

lint:
    pylint src
    pylint --disable=E0401 tests

install:
    pip install -r requirements.txt

install_dev:
    pip install -r .devcontainer/requirements-dev.txt

watch:
    pytest -f

code:
    code README.md justfile

dev:
    python3 src/manage.py runserver

