make rebuild: uninstall build pack_install

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=page_loader --cov-report xml

lint:
	poetry run flake8 page_loader tests

build:
	poetry build

pack_install:
	python3 -m pip install dist/*.whl

uninstall:
	pip uninstall python-project-lvl3