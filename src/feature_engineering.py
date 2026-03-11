#1.load training and testing data
#2.scale the training data
#save scaled data into processed folder
import pickle

from sklearn.discriminant_analysis import StandardScaler
import pandas as pd
from data_preprocessing import load_and_Split_data
X_train,X_test,y_train,y_test=load_and_Split_data()
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(X_train)
x_test_scaled=scaler.transform(X_test)

#3.save scaled data into processed folder
pd.DataFrame(x_train_scaled).to_csv("../data/processed/x_train_scaled.csv",index=False)
pd.DataFrame(x_test_scaled).to_csv("../data/processed/x_test_scaled.csv",index=False)
pd.DataFrame(y_train).to_csv("../data/processed/y_train.csv",index=False)
pd.DataFrame(y_test).to_csv("../data/processed/y_test.csv",index=False)

with open("../artifacts/scaler.pkl","wb") as f:
    pickle.dump(scaler,f)
print("successfully saved the scaler object")