import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model_w = pickle.load(open('model.pkl', 'rb'))
model_s=pickle.load(open('model_s.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/back')
def back():
    return render_template('index.html')


@app.route('/wind')
def wind():
    return render_template('w.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_w.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('w.html', prediction_text='wind genaration should be {} MW 25 sqaure km'.format(output))
@app.route('/solar',)
def solar():
    return render_template('s.html')

@app.route('/predict_s',methods=['POST'])
def predict_s():
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model_s.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('s.html', prediction_text='solar genaration should be {} MW per 25 km2'.format(output))


if __name__ == "__main__":
    app.run(debug=True)