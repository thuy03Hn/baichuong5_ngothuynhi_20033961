# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:15:16 2024

@author: DELL _ PC
"""
N = int(input("Nhập số nguyên dương N: "))
while N <= 0:
    print("Vui lòng nhập số nguyên dương!")
    N = int(input("Nhập lại số nguyên dương N: "))

print("Các ước số của", N, "là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")