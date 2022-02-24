import numpy as np
from .simple_linear_regr_utils import generate_data, evaluate

class SimpleLinearRegression:
    def __init__(self, iterations=2000, lr=0.002):
        self.iterations = iterations # number of iterations the fit method will be called
        self.learning_rate = lr # The learning rate
        self.losses = [] # A list to hold the history of the calculated losses
        self.W, self.b = None, None # the slope and the intercept of the model

    def __calculate_mse(self, difference):
        mse = np.square(difference).mean()
        return mse

    def __calculate_rmse(self, difference):
        mse = np.square(difference).mean()
        rmse = np.sqrt(mse)
        return rmse

    def __calculate_mae(self, difference):
        mae = np.mean(np.abs(difference))
        return mae

    def __calculate_loss(self, y: np.ndarray, y_hat: np.ndarray, loss_metric: str = "MSE"):
        loss = None 
        difference = np.subtract(y, y_hat)

        try: 
            if loss_metric == "RMSE":
                loss = self.__calculate_rmse(difference)
            if loss_metric == "MAE":
                loss = self.__calculate_mae(difference)
            if loss_metric == "MSE":
                loss = self.__calculate_mse(difference)
        except Exception as e:
            print(e)
        
        return loss

    def __loss(self, y: np.ndarray, y_hat: np.ndarray, loss_metric: str = "MSE" ) -> np.float64:
        """

        :param y: the actual output on the training set
        :param y_hat: the predicted output on the training set
        :return:
            loss: the sum of squared error

        """
        #ToDO calculate the loss. use the sum of squared error formula for simplicity
        
        loss = self.__calculate_loss(
            y = y,
            y_hat = y_hat,
            loss_metric = loss_metric 
        )

        self.losses.append(loss)
        return loss

    def __init_weights(self, X):
        """

        :param X: The training set
        """
        weights = np.random.normal(size=X.shape[1] + 1)
        self.W = weights[:X.shape[1]].reshape(-1, X.shape[1])
        self.b = weights[-1]
        print(self.W.shape)
        print(self.b.shape)

    def __sgd(self, X, y, y_hat):
        """

        :param X: The training set
        :param y: The actual output on the training set
        :param y_hat: The predicted output on the training set
        :return:
            sets updated W and b to the instance Object (self)
        """
        # ToDo calculate dW & db.
        n_obs = X.shape[1]
        error = y_hat - y
        dW = (2/n_obs) * sum(X * error)
        db = (2/n_obs) * sum(error)
        #  ToDO update the self.W and self.b using the learning rate and the values for dW and db
        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

    def fit(self, X, y):
        """
        :param X: The training set
        :param y: The true output of the training set
        :return:
        """
        self.__init_weights(X)
        y_hat = self.predict(X)
        loss = self.__loss(y, y_hat)
        print(f"Initial Loss: {loss}")
        for i in range(self.iterations + 1):
            self.__sgd(X, y, y_hat)
            y_hat = self.predict(X)
            loss = self.__loss(y, y_hat)
            if not i % 100:
                print(f"Iteration {i}, Loss: {loss}")


    def predict(self, X):
        """
        :param X: The training dataset
        :return:
            y_hat: the predicted output
        """
        #ToDO calculate the predicted output y_hat. remember the function of a line is defined as y = WX + b
        y_hat = X.dot(self.W) + self.b
        return y_hat

def linear_regression_pipeline():
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    model.fit(X_train,y_train)
    predicted = model.predict(X_test)
    evaluate(model, X_test, y_test, predicted)