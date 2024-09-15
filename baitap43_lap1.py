# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:24:56 2024

@author: DELL _ PC
"""
n= int(input("Nhập số n:"))
S = 0
for i in range(1, n+1):
    S += i / (i + 1)
print(S)