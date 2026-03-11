#1.load scaler.pkl and model.pkl files
#2.create a function to predict
import pickle
import numpy as np
class Insurance_Prediction:
    def __init__(self):
        self.model=pickle.load(f)
        
    def prediction(self,Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs):
        input=np.array([[Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs]])
        scaled_input=self.scaler.transform(input)
        result=self.model.predict(scaled_input)
        return result
    