# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:15:16 2024

@author: DELL _ PC
"""
while True:
    try:
        n = int(input("Nhập số nguyên dương N: "))
        if n > 0:
            break
        else:
            print("N phải là số nguyên dương. Vui lòng nhập lại.")
# In tất cả các ước số của N
i = 1
print("Các ước số của", n, "là:", end=" ")
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1