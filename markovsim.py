# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:52:28 2016

@author: amitr
#Hidden markov model simulation
"""
import random
import numpy as np
def checkjump(next_pos,sn_start,sn_end,ld_star,ld_end):
     if next_pos in sn_start:
                for i in range(0,len(sn_start)):
                    if next_pos==sn_start[i]:
                        next_pos=sn_end[i]
     elif next_pos in ld_start:
                for i in range(0,len(ld_start)):
                    if next_pos==ld_start[i]:
                        next_pos=ld_end[i]
     return next_pos
def posupdate(current_pos,r,probabilities,sn_start,sn_end,ld_start,ld_end):
    next_pos=current_pos
    if r<probabilities[0]:
            next_pos=current_pos+1
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    elif r>=probabilities[0] and r< probabilities[1]:
            next_pos=current_pos+2
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    elif r>=probabilities[1] and r< probabilities[2]:
            next_pos=current_pos+3
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    elif r>=probabilities[2] and r< probabilities[3]:
            next_pos=current_pos+4
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    elif r>=probabilities[3] and r< probabilities[4]:
            next_pos=current_pos+5
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    elif r>=probabilities[4] and r< probabilities[5]:
            next_pos=current_pos+6
            next_pos=checkjump(next_pos,sn_start,sn_end,ld_start,ld_end)
    if next_pos>100:
        next_pos=current_pos
    return next_pos      
    
N=int(input())
sol=[]
for i in range(0,N):
    probabilities=[];Nsnakes=0;Nladders=0;
    sn_start=[];ld_start=[];sn_end=[];ld_end=[]
    current_pos=1;dice_roll_ctr=0;game_ctr=0
    pr=input().split(",")
    for p in pr:
        probabilities.append(float(p))
    nsnld=input().split(",")
    Nsnakes=int(nsnld[1]);Nladders=int(nsnld[0])
    ldrs=input().split(" ")
    snks=input().split(" ")
    for l in ldrs:
        t=l.split(",")
        ld_start.append(int(t[0]));ld_end.append(int(t[1]))
    for s in snks:
        t=s.split(",")
        sn_start.append(int(t[0]));sn_end.append(int(t[1]))
    ## Cumulative probabilities:
    tmp=[];sm=0
    for p in probabilities:
        sm+=p
        tmp.append(sm)
    probabilities=tmp  
    ### Simulation Begins
    final_dic_ct=[];dice_roll_ctr=0
    while game_ctr<5000:
        r=round(random.random(),2)
        dice_roll_ctr+=1
        #print(dice_roll_ctr)
        next_pos=posupdate(current_pos,r,probabilities,sn_start,sn_end,ld_start,ld_end)
        current_pos=next_pos
        if dice_roll_ctr>=1000:
            game_ctr+=1
        elif dice_roll_ctr<1000 and current_pos==100:
            final_dic_ct.append(dice_roll_ctr)
            dice_roll_ctr=0
            current_pos=1
            game_ctr+=1
    #print(final_dic_ct)
    temp=np.asarray(final_dic_ct)
    sol.append(int(np.mean(temp)))
for i in sol:
    print(i)    
            
        
        
        
