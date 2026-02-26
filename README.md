# air-quality-predictor
“Hyper-local air quality prediction with IDW &amp; PM2.5 forecasting”
# 🌬️ Breath Analyzer – Hyper-Local Air Quality Predictor

A predictive air-quality engine using **Spatial Interpolation (IDW)**, **PM2.5 forecasting**, **dynamic heatmaps**, and **automated alerts**.  
Built for **Eco-Hackathon – Round 2 Prototype Submission**.

---

## ⭐ 1. Project Overview

City-wide air quality averages hide the real pollution differences between specific traffic junctions and clean areas.  
This project solves the **data blindspot** by estimating AQI at any location and predicting upcoming pollution levels.

The system includes:
- Blind-spot AQI estimation (IDW interpolation)
- PM2.5 12–24 hour prediction (ML-ready)
- Red Zones (hazardous) and Green Corridors (safe)
- Interactive map with user location marker
- Automatic alerts when entering a polluted area

This prototype demonstrates core logic for proof-of-concept.

---

## ⭐ 2. Features

✔ Interactive pollution map using Leaflet  
✔ Red (High-pollution) & Green (Safe) zones  
✔ Live marker movement with alerts  
✔ PM2.5 predicted value display  
✔ Simple, clean prototype UI  
✔ Works directly in browser (no installation needed)  

---

## ⭐ 3. Tech Stack

| Component | Technology Used |
|----------|------------------|
| Frontend | HTML, CSS, JavaScript |
| Maps     | Leaflet.js + OpenStreetMap |
| Backend (optional for ML) | Python, Pandas, Scikit-Learn |

---

## ⭐ 4. How to Run the Website

### 🔹 Option 1 — Easiest
Just double-click `index.html` → it opens in your browser.

### 🔹 Option 2 — Using VS Code + Live Server
1. Open folder in VS Code  
2. Install **Live Server** extension  
3. Right-click `index.html` → **Open with Live Server**

---

## ⭐ 5. Folder Structure
air-quality-predictor/
│── index.html → Main working prototype (map + heatmap + alerts)
│── app.py → Placeholder backend (for ML integration)
│── README.md → Project documentation
│── output.md → Notes / additional explanation

---

## ⭐ 6. How the Prototype Works

### 🔸 Interpolation (IDW)
Estimates pollution at locations where no sensor exists by giving more weight to nearby stations.

### 🔸 Prediction (ML Model – optional)
Predicts PM2.5 for the next 12–24 hours using weather + historical data  
(Custom model can be added in `app.py` later.)

### 🔸 Visualization
- Red zone → hazardous area  
- Green zone → safe corridor  
- Click on map → moves user marker  
- If marker enters red zone → automatic alert appears  

---

## ⭐ 7. Demo Video  
🎥 *(Will be added during submission)*  
The video will show:
- Map working  
- Prediction value  
- Alerts  
- Code snippet  

---

## ⭐ 8. Future Enhancements  
- Real-time sensor integration  
- Advanced ML forecasting (LSTM / RF)  
- Pollution-safe route planning  
- Exposure calculation for each user  

