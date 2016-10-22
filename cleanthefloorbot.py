# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:05:26 2016

@author: amitr
"""

# cleanthefloorbot
def nextMove(posr, posc, board):
    r=posr;c=posc;grid=board
    for j in range(0,5):
       if grid[r][j]=='d':
          if j>c:
              mov="RIGHT"
          elif j<c:
              mov="LEFT"
          else:
              mov="CLEAN"
    for j in range(0,5):
        if 'd' in grid[j][:]:
            if j>r:
                mov="DOWN"
            elif j<r:
                mov="U
    return mov
n = 5
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(r,c,grid)
