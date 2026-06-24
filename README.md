# 🌍 AirPulse – AI-Powered Air Quality Monitoring Dashboard

## Overview

AirPulse is an AI-powered environmental monitoring dashboard that predicts Air Quality Index (AQI), visualizes air quality across India, identifies pollution hotspots, and provides air-quality alerts.

The project combines Machine Learning, Geospatial Visualization, and Environmental Analytics into a single interactive platform.

---

## Features

### 📍 City-Wise AQI Monitoring

* Delhi
* Mumbai
* Chennai
* Bangalore
* Hyderabad
* Nellore

### 🗺️ Interactive India AQI Map

* Color-coded AQI markers
* National-level visualization
* City-based monitoring

### 🤖 AI-Based AQI Prediction

* Machine Learning model built using XGBoost
* Predicts AQI using environmental parameters
* Real-time dashboard interaction

### 🚨 AQI Alert System

* Good Air Quality
* Moderate Air Quality
* Poor Air Quality
* Hazardous Air Quality

### 🔥 HCHO Hotspot Detection

Identifies high-risk pollution regions such as:

* Delhi NCR
* Mumbai Industrial Belt
* Visakhapatnam Industrial Zone
* Nellore Industrial Area

### 📈 AQI Trend Forecast

* Weekly AQI trend visualization
* Interactive charts using Plotly

---

## Technology Stack

### Frontend

* Streamlit

### Machine Learning

* XGBoost
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Folium
* Streamlit-Folium

### Deployment

* GitHub
* Streamlit Community Cloud

---

## Project Structure

```text
AirPulse/
│
├── app.py
├── train_model.py
├── test_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── aqi_data.csv
│
└── models/
    └── aqi_model.pkl
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rajiv-gowda/AirPulse.git
cd AirPulse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Live Demo

Streamlit Deployment:
https://airpulse-ye9zzrkjhd5vpujqbmv2w4.streamlit.app

GitHub Repository:
https://github.com/rajiv-gowda/AirPulse

---

## Future Enhancements

* Satellite-based AQI estimation
* Real-time AQI APIs
* CPCB and IMD data integration
* 24–72 hour AQI forecasting
* State-wise AQI analytics
* Pollution heatmaps
* Mobile application support

---

## Author

**PANDI RAJIV**

B.Tech – Electronics and Communication Engineering (ECE)

Narayana Engineering College, Nellore

---

## License

This project is developed for educational, research, and environmental monitoring purposes.
