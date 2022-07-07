from distutils.log import debug
from flask import Flask, render_template, request
import pickle
import numpy as np


model = pickle.load(open('Frequency_set.pkl','rb'))

app = Flask(__name__)


@app.route('/')

def man():
    return render_template('index.html')

@app.route('/predict', method = ['POST'])

def index():
    CapShape = request.form['CapShape'];
    CapSurface = request.form['CapSurface'];
    CapColor = request.form['CapColor'];
    Bruises =request.form['Bruises'];
    Ordor = request.form['Ordor'];
    GillAttachment = request.form['GillAttachment'];
    GillSpacing = request.form['GillSpacing'];
    GillSize = request.form['GillSize'];
    GillColor = request.form['GillColor'];
    StalkShape = request.form['StalkShape'];
    StalkRoot = request.form['StalkRoot'];
    StalkSurfaceAboveRing = request.form['StalkSurfaceAboveRing'];
    StalkSurfaceBelowRing =request.form['StalkSurfaceBelowRing'];
    StalkColorAboveRing =request.form['StalkColorAboveRing'];
    StalkColorBelowRing = request.form['StalkColorBelowRing'];
    VeilColor = request.form['VeilColor'];
    RingNumber = request.form['RingNumber'];
    RingType =request.form['RingType'];
    SporePrintColor = request.form['SporePrintColor'];
    Population = request.form['Population'];
    Habitat =request.form['Habitat'];



    arr = np.array([CapShape,CapSurface,CapColor,Bruises,Ordor,GillAttachment,GillSpacing,GillSize,GillColor, StalkShape,StalkRoot,StalkSurfaceAboveRing,StalkSurfaceBelowRing,StalkColorAboveRing,StalkColorBelowRing,VeilColor,  RingNumber, RingType,  SporePrintColor, Population, Habitat])

    pred = model.predict(arr)

    return render_template('predict.html', data = pred)


if __name__ == "__main__":
    app.run(debug= True)
