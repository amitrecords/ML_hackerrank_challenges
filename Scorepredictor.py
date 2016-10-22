# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:56:50 2016

@author:A
"""
import sys
import numpy as np
from sklearn import svm
pscores=input().strip(" ")
print(pscores)
#hscores=sys.stdin.readline().strip('').split(" ")
#print(pscores)
#print(hscores)
clf=svm.SVC(gamma=0.01,C=100.)
