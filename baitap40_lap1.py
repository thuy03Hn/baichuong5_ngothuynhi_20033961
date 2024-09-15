# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:22:47 2024

@author: DELL _ PC
"""
n= int(input("Nhập số n:"))
S = 0
for i in range(1, n+1):
    S += 1 / (2 * i)
print(S)