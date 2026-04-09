from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

model = joblib.load("model/predictive_maintenance_model.plk")
print("fdsfdf")
# Get model


@app.get("/")
def home():
    return {"getting predictive maintenence model api"}


@app.post("/predict")
def predict(data: dict):
    features = np.array([
        data["type"],                # 1st: Type
        data["air_temperature"],     # 2nd: Air
        data["process_temperature"],  # 3rd: Process
        data["rotational_speed"],    # 4th: Speed
        data["torque"],              # 5th: Torque
        data["tool_wear"]            # 6th: Wear
    ]).reshape(1, -1)

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}


# predicts failure
# {
#   "type": 1,
#   "air_temperature": 304.5,
#   "process_temperature": 315.0,
#   "rotational_speed": 2800,
#   "torque": 75.0,
#   "tool_wear": 240
# }


# predict no failure
# {
#   "type": 0,
#   "air_temperature": 298.1,
#   "process_temperature": 308.6,
#   "rotational_speed": 1550,
#   "torque": 42.8,
#   "tool_wear": 0
# }
