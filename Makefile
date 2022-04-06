lint:
	poetry run flake8 page_loader tests

build:
	poetry build

pack_install:
	python3 -m pip install dist/*.whl

make test:
	poetry run pytest

make test-cov:
	poetry run pytest --cov=page_loader --cov-report xml
