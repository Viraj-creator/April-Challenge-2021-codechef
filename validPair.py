# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:27:03 2021

@author: raj patil
"""

A,B,C = map(int,input().split())

if A == B or B == C or A == C:
    print("YES")
else:
    print("NO")
