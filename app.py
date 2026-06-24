import streamlit as st
import joblib
import plotly.express as px
import pandas as pd
import folium
from streamlit_folium import st_folium

# Page Config
st.set_page_config(
    page_title="AirPulse",
    page_icon="🌍",
    layout="wide"
)

# Sidebar
st.sidebar.title("🌍 AirPulse")
st.sidebar.info(
    """
    AI-powered Air Quality Monitoring Dashboard

    Features:
    • AQI Prediction
    • Air Quality Status
    • Weekly AQI Forecast
    • Interactive Dashboard
    • India AQI Map
    """
)

# Load Model
model = joblib.load("models/aqi_model.pkl")

# Title
st.title("🌍 AirPulse AQI Predictor")
st.caption("AI-powered Air Quality Prediction using XGBoost and Streamlit")

# City Selection
st.subheader("📍 Location Selection")

city = st.selectbox(
    "Select City",
    ["Delhi", "Mumbai", "Chennai", "Bangalore", "Hyderabad", "Nellore"]
)

st.success(f"📍 Selected City: {city}")

# City Data
city_data = {
    "Delhi": [38, 45, 5],
    "Mumbai": [32, 75, 12],
    "Chennai": [35, 70, 10],
    "Bangalore": [28, 65, 15],
    "Hyderabad": [34, 55, 8],
    "Nellore": [33, 68, 11]
}

city_coordinates = {
    "Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Chennai": [13.0827, 80.2707],
    "Bangalore": [12.9716, 77.5946],
    "Hyderabad": [17.3850, 78.4867],
    "Nellore": [14.4426, 79.9865]
}

# India AQI Data
india_aqi = [
    ["Delhi", 28.6139, 77.2090, 280],
    ["Mumbai", 19.0760, 72.8777, 150],
    ["Chennai", 13.0827, 80.2707, 120],
    ["Bangalore", 12.9716, 77.5946, 90],
    ["Hyderabad", 17.3850, 78.4867, 170],
    ["Nellore", 14.4426, 79.9865, 95]
    
]

st.write(f"📌 Coordinates: {city_coordinates[city]}")

# India Map
st.subheader("🗺️ India AQI Map")

india_map = folium.Map(
    location=[22.9734, 78.6569],
    zoom_start=5
)
st.subheader("🔥 HCHO Hotspot Detection")

hotspots = [
    ["Delhi NCR", "Very High"],
    ["Mumbai Industrial Belt", "High"],
    ["Visakhapatnam Industrial Zone", "High"],
    ["Nellore Industrial Area", "Moderate"]
]
hotspot_df = pd.DataFrame({
    "Hotspot": ["Delhi NCR", "Mumbai Industrial Belt", "Visakhapatnam", "Nellore"],
    "Risk Level": ["Very High", "High", "High", "Very High"]
})

st.dataframe(hotspot_df, use_container_width=True)



# AQI City Markers
for city_name, lat, lon, aqi_value in india_aqi:

    if aqi_value <= 100:
        color = "green"
    elif aqi_value <= 200:
        color = "orange"
    else:
        color = "red"

    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        popup=f"{city_name} - AQI: {aqi_value}",
        color=color,
        fill=True,
        fill_color=color
    ).add_to(india_map)

# HCHO Hotspot Markers
hotspot_locations = [
    ["Delhi NCR", 28.7041, 77.1025],
    ["Mumbai Industrial Belt", 19.0760, 72.8777],
    ["Visakhapatnam Industrial Zone", 17.6868, 83.2185],
    ["Nellore Industrial Area", 14.4426, 79.9865]
]

for hotspot, lat, lon in hotspot_locations:
    folium.Marker(
        [lat, lon],
        popup=f"🔥 HCHO Hotspot: {hotspot}",
        icon=folium.Icon(color="red", icon="fire")
    ).add_to(india_map)

st_folium(
    india_map,
    width=900,
    height=500
)

# Weather Values
temperature = city_data[city][0]
humidity = city_data[city][1]
wind_speed = city_data[city][2]

st.write(f"🌡 Temperature: {temperature} °C")
st.write(f"💧 Humidity: {humidity} %")
st.write(f"🌬 Wind Speed: {wind_speed} km/h")

# Prediction
st.subheader("🌤 AQI Prediction")

if st.button("Predict AQI"):

    prediction = model.predict(
        [[temperature, humidity, wind_speed]]
    )

    aqi = prediction[0]

    st.metric("Predicted AQI", f"{aqi:.2f}")

    # Alert System
    if aqi > 250:
        st.error(
            f"""
🚨 HAZARDOUS AIR QUALITY ALERT

Location: {city}

AQI: {aqi:.0f}

Avoid outdoor activities and wear an N95 mask.
"""
        )
    elif aqi > 150:
        st.warning(
            f"""
⚠️ AIR QUALITY WARNING

Location: {city}

AQI: {aqi:.0f}

Sensitive groups should limit outdoor exposure.
"""
        )

    # AQI Status
    if aqi <= 50:
        st.success("🟢 Good Air Quality")
    elif aqi <= 100:
        st.info("🟡 Moderate Air Quality")
    elif aqi <= 200:
        st.warning("🟠 Poor Air Quality")
    else:
        st.error("🔴 Hazardous Air Quality")

    # Forecast Chart
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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Footer
st.markdown("---")
st.caption("AirPulse © 2026 | Developed by PANDI RAJIV")