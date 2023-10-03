# This file is used to read in the trained model that was saved as a pkl file

# Import the dependencies
import numpy as np
import tensorflow as tf
from tensorflow import keras

# load model from pickle file

import pickle

o_model_pkl_file = "pickle_ml_test/obesity_linear_regression_dnn_model.pkl" 
c_model_pkl_file = "pickle_ml_test/cancer_linear_regression_dnn_model.pkl"  
d_model_pkl_file = "pickle_ml_test/diabetes_linear_regression_dnn_model.pkl" 
 

# define the function that loads the model into the Flask framework `app.py`
def read_om_model():
    with open(o_model_pkl_file, 'rb') as file:  
        o_model = pickle.load(file)
        return o_model
def read_c_model():
    with open(c_model_pkl_file, 'rb') as file:  
        c_model = pickle.load(file)
        return c_model   
def read_d_model():
    with open(d_model_pkl_file, 'rb') as file:  
        d_model = pickle.load(file)
        return d_model    

 # define input
# this function gets called in the `app.py` file when the javascript detects a change 
# takes the input from the d3.select function and 
def om_predict(o_model, a,b,c,d,e,f,g,h,i):
    # Create a NumPy array from the string variables
    float_array = np.array([a, b, c, d, e, f, g, h, i], dtype=float)

    # Convert the NumPy array to a list if needed
    float_list = float_array.tolist()
    new_input = [float_list]    
    

    return o_model.predict(new_input)


# used for debugging
# with open(o_model_pkl_file, 'rb') as file:  
#         o_model = pickle.load(file)

# new_input = [[4.121429,24.8,18.4, 44.0, 73.2, 33.0, 36.1, 16.9, 28.8]]
# new_output = o_model.predict(new_input)
#     # summarize output
# print(new_output[0])


def all_predict(o_model,c_model, d_model, a,b,c,d,e,f,g,h,i):
    # Create a NumPy array from the string variables
    float_array = np.array([a, b, c, d, e, f, g, h, i], dtype=float)

    # Convert the NumPy array to a list if needed
    float_list = float_array.tolist()
    new_input = [float_list]    
    
    model_list= [o_model,c_model, d_model]
    predictions = []


    for model in model_list:
        prediction = model.predict(new_input)
        print(prediction[0][0])
        predictions.append(prediction[0][0])
    return predictions

#############################
# debugging area
# c_model = read_c_model()
# d_model = read_d_model()
# predictions = all_predict(o_model, c_model, d_model,4.121429,24.8,18.4, 44.0, 73.2, 33.0, 36.1, 16.9, 28.8)

# print(type(all_predict(o_model, c_model, d_model,4.121429,24.8,18.4, 44.0, 73.2, 33.0, 36.1, 16.9, 28.8)))
# print(all_predict(o_model, c_model, d_model,4.121429,24.8,18.4, 44.0, 73.2, 33.0, 36.1, 16.9, 28.8)[0])
# print(type(predictions))
# print(predictions[0])
# print(predictions[1])
# print(predictions[2])

