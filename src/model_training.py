import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# load processed data
X_train = pd.read_csv("data/processed/x_train_scaled.csv")
y_train = pd.read_csv("data/processed/y_train.csv")

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# save model
with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")