import sys
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

####### READING INPUT TRAINING DATA
F,N=sys.stdin.readline().strip().split(' ')
F,N=[int(F),int(N)]
X=[];y=[]
for i in range(0,N):
    lin=sys.stdin.readline().strip().split(' ')
    lin=list(map(float,lin))
    X.append(lin)
Xfeatures=np.asarray(list(row[0:F] for row in X));y=np.asarray(list(row[F] for row in X))
model = make_pipeline(PolynomialFeatures(F), Ridge())
model.fit(Xfeatures, y)
m=int(input())
x=[]
for i in range(0,m):
    lin=sys.stdin.readline().strip().split(' ')
    lin=list(map(float,lin))
    x.append(lin)
X_new=np.asarray(x)
y_new=model.predict(X_new)
for y in y_new:
    print(y)
#y_plot = model.predict(X_plot)