from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import math

app = Flask(__name__)

# -----------------------------
# 1. SAMPLE TRAINING DATA
# -----------------------------
# In real life you will use real AQI + weather data
data = {
    "pm25":      [60, 80, 120, 150, 90, 110],   # past PM2.5
    "temp":      [28, 30, 32, 31, 29, 30],      # temperature data
    "humidity":  [65, 70, 50, 80, 75, 60]        # humidity data
}

df = pd.DataFrame(data)

X = df[["temp", "humidity"]]
y = df["pm25"]

model = RandomForestRegressor()
model.fit(X, y)

# -----------------------------
# 2. FORECAST ENDPOINT
# -----------------------------
@app.route("/predict", methods=["GET"])
def predict():
    # In real world, get live weather data (API)
    temp = float(request.args.get("temp", 30))
    humidity = float(request.args.get("humidity", 60))

    pred = model.predict([[temp, humidity]])[0]
    pred = round(pred, 2)

    return jsonify({"pm25_prediction": pred})


# -----------------------------
# 3. HEATMAP ENDPOINT
# -----------------------------
@app.route("/heatmap", methods=["GET"])
def heatmap():
    points = [
        {"lat": 13.05, "lon": 80.25, "value": 160},  
        {"lat": 13.10, "lon": 80.28, "value": 40},   
        {"lat": 13.08, "lon": 80.27, "value": 70}    
    ]
    return jsonify(points)


# -----------------------------
# 4. ALERT ENDPOINT
# -----------------------------
@app.route("/alert", methods=["GET"])
def alert():
    user_lat = float(request.args.get("lat"))
    user_lon = float(request.args.get("lon"))

    # Red zone center
    red_lat, red_lon = 13.05, 80.25

    # Distance function
    def distance(lat1, lon1, lat2, lon2):
        return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

    dist = distance(user_lat, user_lon, red_lat, red_lon)

    if dist < 0.02:  # threshold distance
        return jsonify({"alert": True, "message": "High pollution zone ahead!"})
    else:
        return jsonify({"alert": False, "message": "Safe zone"})


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)