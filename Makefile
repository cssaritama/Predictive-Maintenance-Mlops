.PHONY: setup lint format test run docker-build docker-run clean

setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install

lint:
	black --check .
	isort --check-only .
	flake8 src tests

format:
	black .
	isort .

test:
	pytest tests/

run:
	uvicorn deployment.main:app --reload

docker-build:
	docker build -t predictive-maintenance:latest deployment/

docker-run:
	docker run -p 8000:8000 predictive-maintenance:latest

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
