# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:25:36 2024

@author: DELL _ PC
"""
n= int(input("Nhập số n:"))
x= int(input("Nhập số n:"))
S = 0

for i in range(1, n+1):
    # Tính tổng của các số nguyên từ 1 đến i
    tong = 0
    for j in range(1, i+1):
        tong += j
    
    # Tính phân số và cộng vào tổng S
    S += tong / (x ** i)

print(S)
