# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 01:34:13 2016

@author: amitr
"""
# findprincess2
def nextMove(n,r,c,grid):
    man=[r,c];princess=[]
    #print(grid_mat)
    for idx,row in enumerate(grid):
        #print(idx)
        for i in range(0,len(row)):
           # print(i)
            if row[i]=='p':
                princess=[idx,i]
    print(princess)
    if man[0]<princess[0]:
        mov="DOWN"
    elif man[0]>princess[0]:
        mov="UP"
    elif man[1]<princess[1]:
        mov="RIGHT"
    elif man[1]>princess[1]:
        mov="LEFT"
    return mov
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
