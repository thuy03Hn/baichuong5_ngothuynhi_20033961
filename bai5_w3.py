# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:01:42 2024

@author: DELL _ PC
"""
#a 
j = 0
for i in range(0, 10):
    j += i
print(j)  # Kết quả là 45
#b
j = 1
for i in range(0, 10):
    j += j
print(j)  # Kết quả là 1024
#c
j = 0
for j in range(0, 10):
    j += j
print(j)  # Kết quả là 18
#d
