# Predictive Maintenance MLOps Project

This project implements an end-to-end MLOps pipeline to predict equipment failures using sensor data. 
It leverages MLflow for experiment tracking, Prefect for orchestration, FastAPI for model deployment, 
Terraform for infrastructure provisioning, Evidently for monitoring, and GitHub Actions for CI/CD.

## Project Structure

```
├── README.md
├── requirements.txt
├── Makefile
├── .pre-commit-config.yaml
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_inference.py
│   └── monitoring.py
├── flows/
│   └── prefect_pipeline.py
├── deployment/
│   ├── main.py
│   ├── Dockerfile
│   └── terraform/
├── tests/
│   ├── test_training.py
│   └── test_inference.py
└── .github/workflows/ci-cd.yml
```

## Setup Instructions

1. Clone the repo
2. Install dependencies: `make setup`
3. Run tests: `make test`
4. Run the API: `make run`
5. Build Docker image: `make docker-build`
6. Deploy infrastructure with Terraform (see deployment/terraform/README.md)

## Usage

- Train model and log experiments with MLflow
- Orchestrate pipeline using Prefect (`flows/prefect_pipeline.py`)
- Use FastAPI at `/predict` endpoint for inference
- Monitor data and model drift with Evidently and Prometheus
- CI/CD automated via GitHub Actions
