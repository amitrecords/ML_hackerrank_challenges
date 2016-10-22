import math
import statistics as stat
trades=[[99.0,5.0,20.0],[95.0,15.0,10.0],[60.0,30.0,50.0],[80.0,40.0,60.0],[5.0,80.0,40.0],[3.0,92.0,20.0]]
labels=['green','green','blue','blue','red','red']
new_trades=[[90.0,10.0,15.0],[10.0,98.0,50.0],[55.0,25.0,33.0],[2.0,80.0,26.0]]
N=len(trades)
greentrades=[];redtrades=[];unique_label=[];
############ Geting mean of a class trade
def getmean(trade):
    sm1=0;sm2=0;sm3=0
    Ng=len(trade)
    for t in trade:
        sm1+=t[0];sm2+=t[1];sm3+=t[2]
    tmean=[sm1/Ng,sm2/Ng,sm3/Ng]
    return(tmean)
###########Geting unique Labels
def getuniquelabels(labels):
    unique_labels=[];
    for i in range(0,len(labels)):
        if labels[i] in unique_labels:
            pass
        else:
            unique_labels.append(labels[i])
    return (unique_labels)
    
###########Finding distance between a trade and a mean point of class 
def getdist(trade,lmeans):
    t=trade;
    Xg=(t[0]-lmeans[0])**2+(t[1]-lmeans[1])**2+(t[2]-lmeans[2])**2
    distg=math.sqrt(Xg)
    return distg
###### Main body
unique_label=getuniquelabels(labels)
unique_label_trades=[]

for i in range(0,len(unique_label)):
    tmp_trades=[]
    for t in range(0,len(trades)):
        if labels[t]==unique_label[i]:
            tmp_trades.append(trades[t])
    unique_label_trades.append(tmp_trades)
class_means=[]
for clas in unique_label_trades:
    class_means.append(getmean(clas))
new_labels=[]
for t in new_trades:
    dist=[]
    for i in class_means:
        dist.append(getdist(t,i))
    min=dist[0];minlabel=0;
    for d in range(0,len(dist)):
        if dist[d]< min:
            min=dist[d]
            minlabel=d
    new_labels.append(unique_label[minlabel])
print(new_labels)       
    