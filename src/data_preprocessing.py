#load raw data
#2.Identify x and y values(input or output)
#3.split data into train and test set
import pandas as pd
from sklearn.model_selection import train_test_split
def load_and_Split_data():
    data=pd.read_csv("../data/raw/insurance_dataset.csv")
    X=data[['Age','Annual_Income_LPA','Policy_Term_Years','Sum_Assured_Lakhs']]
    y=data['Annual_Premium_Thousands']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    print("Training data shape:", X_train.shape)
    print("Testing data shape:", X_test.shape)
    return X_train,X_test,y_train,y_test
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_Split_data()
    print("Train shape:", X_train.shape)
    print("Test shape:", X_test.shape)