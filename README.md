# mlflow_example

- mlflow server --backend-store-uri sqlite:///./backend/mlflow.db --host 127.0.0.1 --port 5000

- mlflow models serve -m "models:/ElasticnetWineModel/Staging" -p 1234 --no-conda
