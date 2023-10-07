install:
	echo "🚀 Creating virtual environment using pyenv and poetry"
	poetry install
	poetry run pre-commit install
	#poetry shell

check:
	echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	poetry lock --check
	echo "🚀 Linting code: Running pre-commit"
	poetry run pre-commit run -a
	echo "🚀 Static type checking: Running mypy"
	poetry run mypy
	echo "🚀 Checking for obsolete dependencies: Running deptry"
	poetry run deptry .

test:
	echo "🚀 Testing code: Running pytest"
	poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml

build: clean-build
	echo "🚀 Creating wheel file"
	poetry build

clean-build:
	rm -rf dist

publish:
	echo "🚀 Publishing: Dry run."
	poetry config pypi-token.pypi $(PYPI_TOKEN)
	poetry publish --dry-run
	echo "🚀 Publishing."
	poetry publish

build-and-publish: build publish

docs-test:
	poetry run mkdocs build -s

docs:
	poetry run mkdocs serve
