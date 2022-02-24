import pytest
import numpy as np
from galton.simple_linear_regr import SimpleLinearRegression
from galton.simple_linear_regr import load_model

model = load_model("./artifacts/simple_linear_regression.pkl")

sample_y = np.array(
    [1, 2, 3, 4]
)

sample_y_hat = np.array(
    [2, 2, 3 , 2]
)

sample_X = np.array(
    [
        [1],
        [2],
        [3],
        [4]
    ]
)

def test_mse_loss_calculation():
    mse_loss = model._SimpleLinearRegression__calculate_loss(
        sample_y,
        sample_y_hat,
        loss_metric = "MSE"
    )
    assert mse_loss == 1.25

def test_rmse_loss_calculation():
    rmse_loss = model._SimpleLinearRegression__calculate_loss(
        sample_y,
        sample_y_hat,
        loss_metric = "RMSE"
    )
    assert rmse_loss >= 1


def test_mae_loss_calculation():
    mae_loss = model._SimpleLinearRegression__calculate_loss(
        sample_y,
        sample_y_hat,
        loss_metric = "MAE"
    )
    assert mae_loss == 0.75

def test_init_weights():
    model._SimpleLinearRegression__init_weights(sample_X)

    assert model.W is not None
    assert isinstance(model.W, np.ndarray) 
    assert model.b is not None
    assert isinstance(model.b, np.float64)

def test_sgd():
    model.W = 1
    model.b = 1
    model._SimpleLinearRegression__sgd(
        X = sample_X,
        y = sample_y,
        y_hat = sample_y_hat
    )
    assert model.W.tolist() == [
            0.96,
            1,
            1,
            1.08
        ]
    assert model.b == 1.004

def test_predict():
    y_hat =  model.predict(sample_y)
    assert y_hat == 11.284

