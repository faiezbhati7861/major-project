!pip install flask-ngrok
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle
app = Flask(__name__)
from keras.models import load_model
# Feature Scaling
# Standard Scaling:  Standardization = X'=X-mean(X)/standard deviation
# normal scaling : Normalization= X'=X-min(X)/max(x)-min(X)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
run_with_ngrok(app)
@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  Traffic_signal = int(request.args.get('Traffic_signal'))
  Rain = int(request.args.get('Rain')) 
  
  
  y_pred= model.predict(sc_X.transform(np.array([[Traffic_signal,Rain]])))
  y_pred = (y_pred > 0.5)
  if y_pred>0.5:
    result="survival is not possible"
  else:
    result="survival is not possible"
        
  return render_template('index.html', prediction_text='Model  has predicted  : {}'.format(result))


app.run()