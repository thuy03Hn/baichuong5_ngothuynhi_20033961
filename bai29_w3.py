# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:39:08 2024

@author: DELL _ PC
"""

n= int(input("Nhập số nguyên n: "))

if n > 0:
    for i in range(1, n + 1):
        dong = ""
        for j in range(1, n + 1):
            if i % j == 0 and j % i == 0:  # Xác định nếu i và j là số nguyên tố cùng nhau
                dong += "*"
            else:
                dong += " "
        print(dong)
else:
    print("n phải là số nguyên dương.")