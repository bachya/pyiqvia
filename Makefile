clean:
	pipenv --rm
coverage:
	pipenv run py.test -s --verbose --cov-report term-missing --cov-report xml --cov=iqvia tests
init:
	pip3 install --upgrade pip pipenv
	pipenv lock
	pipenv install --three --dev
lint:
	pipenv run flake8 iqvia
	pipenv run pydocstyle iqvia
	pipenv run pylint iqvia
publish:
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	rm -rf dist/ build/ .egg iqvia.egg-info/
test:
	pipenv run py.test
typing:
	pipenv run mypy --ignore-missing-imports iqvia
