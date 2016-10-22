# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:26:11 2016

@author: amitr
"""
###### Find the Princess!
def displayPathtoPrincess(grid_mat,grid):
    man=[];princess=[]
    for idx,row in enumerate(grid):
        #print(idx)
        for i in range(0,len(row)):
            if row[i]=='m':
                man=[idx+1,grid_mat[idx][i]]
            elif row[i]=='p':
                princess=[idx+1,grid_mat[idx][i]]
    while man!=princess:
        if man[0]<princess[0]:
            print("DOWN")
            man[0]+=1
        elif man[0]>princess[0]:
            print("UP")
            man[0]-=1
        elif man[1]<princess[1]:
            print("RIGHT")
            man[1]+=1
        elif man[1]>princess[1]:
            print("LEFT")
            man[1]-=1
    
    
        
#print all the moves here
m = int(input())
grid = []
grid_mat=[]
for r in range(0,m):
    for j in range(0,m):
        grid_mat.append([r+1,j+1])
#print(grid_mat)
for i in range(0, m):
    grid.append(input().strip())
#print(grid)
displayPathtoPrincess(grid_mat,grid)
