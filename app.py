from distutils.log import debug
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        sg = float(request.form['sg'])

        return render_template('predict.html',prediction=1)

if __name__ == "__main__":
    app.run(debug = True)
