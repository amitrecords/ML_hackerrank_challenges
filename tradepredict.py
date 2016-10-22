import math
import statistics as stat
trades=[[99.0,5.0,20.0],[95.0,15.0,10.0],[5.0,80.0,40.0],[3.0,92.0,20.0]]
labels=['green','green','red','red']
new_trades=[[90.0,10.0,15.0],[10.0,98.0,50.0]]
y=[1,1,0,0]
mean1=[];stand1=[]
for i in range(0,3):
    mean1.append(stat.mean([trades[0][i],trades[1][i],trades[2][i],trades[3][i]]))
    stand1.append(stat.stdev([trades[0][i],trades[1][i],trades[2][i],trades[3][i]]))
for i in range(0,len(trades)):
    trades[i][0]=(trades[i][0]-mean1[0])/stand1[0]
    trades[i][1]=(trades[i][1]-mean1[1])/stand1[1]
    trades[i][2]=(trades[i][2]-mean1[2])/stand1[2]
print(trades)
    
def sigmoid(x):
    z=1/(1+math.exp(-x))
    return z
X1=[];X2=[];X3=[]
for t in trades:
    X1.append(t[0])
    X2.append(t[1])
    X3.append(t[2])
theta=[0,0,0,0]
X=trades
alpha=0.01
def costfunc(theta,X,y):
    sm=0;
    for i in range(0,len(y)):
        s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
        sm= sm + (sigmoid(s)-y[i])**2
    J=(1/(2*len(y)))*sm
    return J

def graddesc(theta,X,y):
    for i in range(0,1000):
        sm1=0
        for i in range(0,len(y)):
            s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
            sm1= sm1 + (sigmoid(s)-y[i])
        sm2=0
        for i in range(0,len(y)):
            s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
            sm2= sm2 + (sigmoid(s)-y[i])*X[i][0]
        sm3=0
        for i in range(0,len(y)):
            s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
            sm3= sm3 + (sigmoid(s)-y[i])*X[i][1]
        sm4=0
        for i in range(0,len(y)):
            s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
            sm4= sm4 + (sigmoid(s)-y[i])*X[i][2]
        sum1=sm1
        sum2=sm2
        sum3=sm3
        sum4=sm4
        theta[0]=theta[0]-(1/len(y))*alpha*sum1
        theta[1]=theta[1]-(1/len(y))*alpha*sum2
        theta[2]=theta[2]-(1/len(y))*alpha*sum3
        theta[3]=theta[3]-(1/len(y))*alpha*sum4
        J=costfunc(theta,X,y) 
        print(J)
    return theta

theta=graddesc(theta,X,y)
Xn=new_trades
print(theta)
for i in range(0,2):
    s=theta[0]+theta[1]*X[i][0]+theta[2]*X[i][1]+theta[3]*X[i][2]
    print(s)
    p= sigmoid(s)
    if p>0.5:
        print(p,"green")
    else:
        print(p,"red")
