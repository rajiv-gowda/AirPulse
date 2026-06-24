# 🌍 AirPulse: AI-Powered Air Quality Monitoring & Hotspot Detection Dashboard

## Overview

AirPulse is an AI-powered environmental monitoring dashboard designed to predict Air Quality Index (AQI), visualize air quality across India, detect pollution hotspots, and generate automated air-quality alerts.

The system combines Machine Learning, Geospatial Visualization, Environmental Analytics, and Interactive Dashboards to provide an intuitive air quality monitoring platform.

---

## 🚀 Features

### 📍 City-Wise AQI Monitoring

Monitor AQI conditions for:

* Delhi
* Mumbai
* Chennai
* Bangalore
* Hyderabad
* Nellore

### 🗺️ Interactive India AQI Map

* Color-coded AQI markers
* India-wide visualization
* Interactive geospatial mapping
* City-level monitoring

### 🤖 AI-Powered AQI Prediction

* Built using XGBoost Machine Learning
* Predicts AQI from environmental parameters
* Real-time predictions through an interactive dashboard

### 🚨 AQI Alert System

Automatically categorizes air quality:

* 🟢 Good
* 🟡 Moderate
* 🟠 Poor
* 🔴 Hazardous

Provides health warnings for unsafe AQI levels.

### 🔥 HCHO Hotspot Detection

Identifies high-risk pollution regions:

* Delhi NCR
* Mumbai Industrial Belt
* Visakhapatnam Industrial Zone
* Nellore Industrial Area

### 📈 AQI Trend Forecasting

* Weekly AQI trend visualization
* Interactive charts using Plotly
* Environmental trend analysis

---

## 🛠️ Technology Stack

### Programming Language

* Python

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

### Web Application

* Streamlit

### Deployment

* GitHub
* Streamlit Community Cloud

---

## 📂 Project Structure

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

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/rajiv-gowda/AirPulse.git
cd AirPulse
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

### Streamlit Application

https://airpulse-ye9zzrkjhd5vpujqbmv2w4.streamlit.app

### GitHub Repository

https://github.com/rajiv-gowda/AirPulse

---

## 🎯 Project Objectives

* Predict Air Quality Index using Machine Learning.
* Visualize AQI data through geospatial maps.
* Detect environmental pollution hotspots.
* Generate AQI alerts for public awareness.
* Demonstrate environmental monitoring through AI-powered analytics.

---

## 🔮 Future Enhancements

* Real-time AQI APIs integration
* Satellite-based AQI estimation
* CPCB and IMD data integration
* 24–72 hour AQI forecasting
* State-wise AQI analytics
* Pollution heatmaps
* Mobile application support

---

## 👨‍💻 Author

**Pandi Rajiv**

B.Tech – Electronics and Communication Engineering (ECE)

Narayana Engineering College, Nellore

---

## 📜 License

This project is developed for educational, research, and environmental monitoring purposes.
