import numpy as np
from galton.simple_linear_regr import load_model

def lambda_handler(event, context):
    data = event['payload']
    model = load_model("./artifacts/simple_linear_regression.pkl")
    predictions = [
        model.predict(np.array(row)).item()
        for row in data['payload']
    ]
    return {
        "predictions": predictions
    } 