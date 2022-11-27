# mlflow_example

- Start tracking server
```
mlflow server --backend-store-uri sqlite:///./backend/mlflow.db --host 127.0.0.1 --port 5000
```

- Run
```
python3 train.py
```
- "mlflow run ." needs pyenv with the virtualenv environment manager.

- Start production server
```
mlflow models serve -m "models:/ElasticnetWineModel/Staging" -p 1234 --no-conda
```
