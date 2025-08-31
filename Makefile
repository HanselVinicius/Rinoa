.PHONY: install format lint type-check test

install:
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

format:
	. venv/bin/activate && black src tests && isort src tests

lint:
	. venv/bin/activate && flake8 src tests

type-check:
	. venv/bin/activate && mypy src

test:
	. venv/bin/activate && pytest -v

check-all: format lint type-check