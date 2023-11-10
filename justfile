flt:
    black src tests
    pylint src tests
    pytest

format:
    black src tests

lint:
    pylint src

test:
    pytest

watch:
    pytest -f