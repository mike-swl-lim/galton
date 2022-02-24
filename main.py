from flask import Flask, request
from galton.simple_linear_regr import load_model
import numpy as np
import os

app = Flask(__name__)


@app.route('/batch', methods=['POST'])
def score_batch():
    data = request.get_json(force = True)
    model = load_model("./artifacts/simple_linear_regression.pkl")
    predictions = [
        model.predict(np.array(row)).item()
        for row in data['payload']
    ]
    return {
        "predictions": predictions
    }


@app.route('/stream', methods=['POST'])
def score_stream():
    data = request.get_json(force = True)
    model = load_model("./artifacts/simple_linear_regression.pkl")
    pred = model.predict(np.array(data['payload']))
    return {
        "stream_prediction": pred.tolist()[0]
    }

os.system(
    "export FLASK_APP=main && flask run"
)