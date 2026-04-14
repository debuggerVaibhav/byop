from sklearn.linear_model import LinearRegression
import pandas as pd

def train_model():
    data = pd.read_csv("study-time-predictor/data.csv")

    X = data[["subjects", "difficulty", "days_left"]]
    y = data["study_hours"]

    model = LinearRegression()
    model.fit(X, y)

    return model
