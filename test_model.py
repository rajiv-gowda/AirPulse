import joblib

# Load model
model = joblib.load("models/aqi_model.pkl")

# Example prediction
prediction = model.predict([[33, 60, 10]])

print("Predicted AQI:", prediction[0])