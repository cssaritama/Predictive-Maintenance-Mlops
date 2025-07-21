import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

def load_data(path: str):
    """Load dataset from CSV file."""
    return pd.read_csv(path)

def train_model(data_path: str):
    data = load_data(data_path)

    # Assuming the target column is 'RUL' (Remaining Useful Life)
    X = data.drop(columns=['RUL'])
    y = data['RUL']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        # Define model with hyperparameters
        n_estimators = 100
        max_depth = 10
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        rmse = mean_squared_error(y_val, preds, squared=False)

        # Log parameters, metrics, and model
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, artifact_path="model")

        print(f"Validation RMSE: {rmse:.4f}")

if __name__ == "__main__":
    DATA_PATH = os.getenv("DATA_PATH", "data/maintenance_data.csv")
    train_model(DATA_PATH)
