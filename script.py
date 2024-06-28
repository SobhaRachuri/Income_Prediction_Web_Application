# Importing necessary libraries
import os
import flask
import pickle
import numpy as np
from flask import Flask, render_template, request

# Creating instance of the Flask class
app = Flask(__name__, template_folder='templates1')

# Load the model from the pickle file
model_path = r'C:\Users\R Sobha Supriya\Desktop\income-prediction1\model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Route to render index.html
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Extract the form data
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    to_predict_list = list(map(float, to_predict_list))

    # Convert the input data into numpy array
    input_data = np.array([to_predict_list])

    # Predict using the loaded model
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        result = '>50K'
    else:
        result = '<=50K'

    # Render the result template with the prediction
    return flask.render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
