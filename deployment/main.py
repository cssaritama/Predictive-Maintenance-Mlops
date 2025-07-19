from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import os

app = FastAPI(title="Predictive Maintenance Model API")

# Load model once at startup
MODEL_PATH = os.getenv("MODEL_PATH", "models/latest_model")
model = mlflow.pyfunc.load_model(MODEL_PATH)

class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float
    feature_5: float

@app.get("/")
def root():
    return {"message": "Predictive Maintenance Model API is running"}

@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        input_data = [[
            data.feature_1,
            data.feature_2,
            data.feature_3,
            data.feature_4,
            data.feature_5,
        ]]
        prediction = model.predict(input_data)
        return {"predicted_rul": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
