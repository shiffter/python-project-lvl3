lint:
	poetry run flake8 modules scripts tests

build:
	poetry build

pack_install:
	python3 -m pip install dist/*.whl