# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:32:15 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra số chính phương
i = 1
sochinhphuong = False

while i * i <= n:
    if i * i == n:
        sochinhphuong = True
    i += 1

if sochinhphuong:
    print(n, "là số chính phương.")
else:
    print(n, "không phải là số chính phương.")
    