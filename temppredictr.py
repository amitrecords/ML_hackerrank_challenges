# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:23:27 2016

@author: amitr
"""
#Temperature Predict
#import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
years_list= list(range(1908,2013))
month_list=list(range(1,13))
N=int(input())
N_xlist1=[]
N_xlist2=[]
N_xmissing_tmin=[];N_xmissing_tmax=[]
tmin_list=[];tmax_list=[]
useless=input()
ctr1=0;ctr2=0
for i in range(0,N):
    lin=input().strip().split()
    try:
        tmin=float(lin[2]);
        tmin_list.append(tmin)
        N_xlist1.append(i+1)
    except:
        pass
    try:
        tmax=float(lin[3]);
        tmax_list.append(tmax)
        N_xlist2.append(i+1)
    except:
        pass    
N_xlist1=np.asarray(N_xlist1).reshape(-1,1);N_xlist2=np.asarray(N_xlist2).reshape(-1,1)
y1=np.asarray(tmin_list).reshape(-1,1)
y2=np.asarray(tmax_list).reshape(-1,1)
model1 = make_pipeline(PolynomialFeatures(1), Ridge())
model2 = make_pipeline(PolynomialFeatures(1), Ridge())
model1.fit(N_xlist1, y1)
model2.fit(N_xlist2, y2)
plt.plot(N_xlist1,y1,'r',N_xlist2,y2,'b')
plt.hold(True)
for i in range(1,N+1):
    if i in N_xlist1:
        pass
    else:
        y_new1=model1.predict(i)
        print(round(float(y_new1),1))
        plt.plot(i,y_new1,'ro')
    if i in N_xlist2:
        pass
    else:
        y_new2=model2.predict(i)
        print(round(float(y_new2),1))
        plt.plot(i,y_new2,'bo')

