from galton.simple_linear_regr import linear_regression_pipeline
from galton.simple_linear_regr import save_model

model = linear_regression_pipeline()

save_model(
    model = model,
    save_path = "./artifacts/simple_linear_regression.pkl"
)

### test load