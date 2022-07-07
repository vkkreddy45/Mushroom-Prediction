from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from data_preprocessing import LogisticReg
from data_preprocessing import RandomForest
from data_preprocessing import DecisionTree
from data_preprocessing import Node

model = pickle.load(open('/Users/pavanvasanthkommineni/Desktop/project/Random_Frequency_set.pkl','rb'))
list1=pickle.load(open('/Users/pavanvasanthkommineni/Desktop/project/tt.pkl','rb'))
list2=pickle.load(open('/Users/pavanvasanthkommineni/Desktop/project/tt1.pkl','rb'))

app = Flask(__name__)


@app.route('/')

def man():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])

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



    arr = [CapShape,CapSurface,CapColor,Bruises,Ordor,GillAttachment,GillSpacing,GillSize,GillColor, StalkShape,
            StalkRoot,StalkSurfaceAboveRing,StalkSurfaceBelowRing,StalkColorAboveRing,StalkColorBelowRing,VeilColor,  
            RingNumber, RingType,  SporePrintColor, Population, Habitat]
    rp=[]
    print(list1)
    print(list2)
    for i in range(len(arr)):
        uu=arr[i]
        qp=list1[i]
        for j in range(len(qp)):
            if uu==qp[j]:
                rp.append(j)
    
    print(list1)
    print(list2)
    ppi=[]
    #ppi=[1]   logistic
    for i in range(len(rp)):
        rt=list2[i]
        ppi.append(rt[rp[i]])
    
    c=["cap-shape",	"cap-surface"	,"cap-color"	,"bruises"	,"odor",	"gill-attachment"	,"gill-spacing",	"gill-size"	,"gill-color",	"stalk-shape",	"stalk-root"	,"stalk-surface-above-ring"	,"stalk-surface-below-ring",	"stalk-color-above-ring",	"stalk-color-below-ring","veil-color",	"ring-number"	,"ring-type"	,"spore-print-color"	,"population"	,"habitat"]
    arr1=pd.DataFrame(ppi).T
    arr1.columns=c
    #arr=np.array(ppi)
    pred = model.predict(np.array(arr1))

    return render_template('predict.html', data =int(pred))


if __name__ == "__main__":
    app.run(debug= True)
