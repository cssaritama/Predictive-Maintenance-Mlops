install:
	pip install -r requirements.txt

lint:
	black .
	flake8 .
	isort .
