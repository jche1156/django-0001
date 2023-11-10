format_test_lint:
    black src tests
    pytest
    pylint src tests

watch:
    pytest -f

run:
    python src/main.py

install_dev:
    pip install -r .devcontainer/requirements-dev.txt