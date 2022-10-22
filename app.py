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
        bp = request.form['bp']
        al = request.form['al']
        su = request.form['su']
        rbc = request.form['rbc']
        pc = request.form['pc']
        bgr = request.form['bgr']
        sc = float(request.form['sc'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        htn = request.form['htn']
        appet = request.form['appet']
        pe = request.form['pe']
        print(bp,al,su,rbc,pc,bgr,sc,pot,hemo,htn,appet,pe)
        return render_template('predict.html',prediction=1)

if __name__ == "__main__":
    app.run(debug = True)
