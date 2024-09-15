# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:37:58 2024

@author: DELL _ PC
"""

n = int(input("Nhập kích thước bàn cờ n (số nguyên dương): "))

if n > 0:
    for i in range(n):
        dong = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                dong += "*"
            else:
                dong += " "
        print(dong)
else:
    print("Kích thước bàn cờ phải là số nguyên dương.")