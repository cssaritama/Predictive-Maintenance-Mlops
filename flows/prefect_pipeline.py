from prefect import flow, task
import mlflow
from src.model_training import load_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

@task
def load_and_split_data(path: str):
    data = load_data(path)
    X = data.drop(columns=['RUL'])
    y = data['RUL']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_val, y_train, y_val

@task
def train_and_log_model(X_train, X_val, y_train, y_val):
    n_estimators = 100
    max_depth = 10
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    rmse = mean_squared_error(y_val, preds, squared=False)

    with mlflow.start_run():
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, artifact_path="model")

    return rmse

@flow
def training_pipeline(data_path: str):
    X_train, X_val, y_train, y_val = load_and_split_data(data_path)
    rmse = train_and_log_model(X_train, X_val, y_train, y_val)
    print(f"Model training completed with RMSE: {rmse:.4f}")

if __name__ == "__main__":
    DATA_PATH = os.getenv("DATA_PATH", "data/maintenance_data.csv")
    training_pipeline(DATA_PATH)
