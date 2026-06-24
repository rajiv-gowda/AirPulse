import pandas as pd
from xgboost import XGBRegressor
import joblib

# Load dataset
df = pd.read_csv("data/aqi_data.csv")

# Features
X = df[["temperature", "humidity", "wind_speed"]]

# Target
y = df["AQI"]

# Create model
model = XGBRegressor()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "models/aqi_model.pkl")

print("Model trained and saved successfully!")