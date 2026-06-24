import streamlit as st
import joblib
import plotly.express as px
import pandas as pd
st.set_page_config(
    page_title="AirPulse",
    page_icon="🌍",
    layout="wide"
)
st.sidebar.title("🌍 AirPulse")
st.sidebar.info(
    """
    AI-powered Air Quality Monitoring Dashboard
    
    Features:
    • AQI Prediction
    • Air Quality Status
    • Weekly AQI Forecast
    • Interactive Dashboard
    """
)

# Load trained model
model = joblib.load("models/aqi_model.pkl")

st.title("🌍 AirPulse AQI Predictor")
st.caption("AI-powered Air Quality Prediction using XGBoost and Streamlit")

temperature = st.slider("Temperature (°C)", 0, 50, 30)
humidity = st.slider("Humidity (%)", 0, 100, 60)
wind_speed = st.slider("Wind Speed (km/h)", 0, 50, 10)

if st.button("Predict AQI"):
    prediction = model.predict([[temperature, humidity, wind_speed]])

    aqi = prediction[0]

    st.metric("Predicted AQI", f"{aqi:.2f}")

    if aqi <= 50:
        st.success("🟢 Good Air Quality")
    elif aqi <= 100:
        st.info("🟡 Moderate Air Quality")
    elif aqi <= 200:
        st.warning("🟠 Poor Air Quality")
    else:
        st.error("🔴 Hazardous Air Quality")

    aqi_history = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "AQI": [120, 135, 128, 145, aqi]
    })

    fig = px.line(
        aqi_history,
        x="Day",
        y="AQI",
        title="Weekly AQI Trend Forecast",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")
st.caption("AirPulse © 2026 | Developed by PANDI RAJIV")