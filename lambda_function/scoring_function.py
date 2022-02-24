import numpy as np
from galton.simple_linear_regr import load_model

def lambda_handler(event, context):
    model = load_model("./artifacts/simple_linear_regression.pkl")
    predictions = [
        model.predict(np.array(row)).item()
        for row in event['payload']
    ]
    return {
        "predictions": predictions
    } 