from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and encoder
model = joblib.load("ill_root_cause_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = FastAPI(title="ILL Root Cause Detection API")

# Request schema
class NetworkMetrics(BaseModel):
    latency_ms: float
    packet_loss_: float
    jitter_ms: float
    signal_strength_dbm: float
    device_temperature_C: float
    device_uptime_hours: float
    power_status: int
    bandwidth_usage_: float
    weather_condition: int
    last_maintenance_days: int

@app.get("/")
def home():
    return {"message": "ILL Root Cause Detection API Running"}

@app.post("/predict")
def predict(data: NetworkMetrics):
    
    input_data = np.array([[
        data.latency_ms,
        data.packet_loss_,
        data.jitter_ms,
        data.signal_strength_dbm,
        data.device_temperature_C,
        data.device_uptime_hours,
        data.power_status,
        data.bandwidth_usage_,
        data.weather_condition,
        data.last_maintenance_days
    ]])

    prediction = model.predict(input_data)
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    return {
        "predicted_root_cause": predicted_label
    }
