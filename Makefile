lint:
	poetry run bash -c 'isort . && flake8 --config setup.cfg && black --config pyproject.toml .'

run:
	poetry run python3 -m geocoder -a $(arg)