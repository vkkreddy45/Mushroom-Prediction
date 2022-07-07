from re import X
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from algorithms import LogisticReg
from algorithms import RandomForest
from algorithms import DecisionTree
from algorithms import Node
from algorithms import KNN
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('Random_Frequency_set.pkl','rb'))
list1=pickle.load(open('tt.pkl','rb'))
list2=pickle.load(open('tt1.pkl','rb'))
list3=pickle.load(open('trt.pkl','rb'))
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
    pred=model.predict(np.array(arr1))
    #np.array(arr1) for randomforest
    #arr=np.array(ppi)

    # scaler = StandardScaler()
    # X_train=scaler.fit_transform(list3)
    # X_test = scaler.transform(arr1)
    # pred = model.predict(X_test)

    #[0] for just knn
    return render_template('predict.html', data =int(pred))


if __name__ == "__main__":
    app.run(debug= True)
