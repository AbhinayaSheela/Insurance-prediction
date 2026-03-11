#1.load scaler.pkl and model.pkl files
#2.create a function to predict
import pickle
import numpy as np
import os

class Insurance_Prediction:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.normpath(os.path.join(base_dir, "../artifacts/model.pkl"))
        scaler_path = os.path.normpath(os.path.join(base_dir, "../artifacts/scaler.pkl"))

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(scaler_path, "rb") as f:
            self.scaler = pickle.load(f)

    def prediction(self, Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs):

        input_data = np.array([[Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs]])

        scaled_input = self.scaler.transform(input_data)

        result = self.model.predict(scaled_input)

        return result[0]
    