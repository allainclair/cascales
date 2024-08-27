clean:
	rm -rf .venv uv.lock .sesskey

install-python:
	uv python install 3.12

dev-run: install-python  # Rich is a package to pretty print.
	uv run --with rich uvicorn --host 0.0.0.0 app.main:app --reload

run: install-python
	uv run uvicorn --host 0.0.0.0 app.main:app

# Lint tools
ruff: install-python
	uvx ruff check .

ruff-fix: install-python
	uvx ruff check . --fix

ruff-format: install-python
	uvx ruff format

mypy: install-python  # check why not finding "import no found"
	uv sync
	uvx mypy --strict .

lint: ruff mypy

# Debug tools
uvx-ipython: install-python
	uvx ipython

uvx-ptw: install-python  # Must improve this command to have pytest installed.
	uvx --from pytest-watcher ptw .
