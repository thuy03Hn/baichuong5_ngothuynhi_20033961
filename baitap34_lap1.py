# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:34:56 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra số nguyên tố
nguyento = True

if n <= 1:
    nguyento = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            nguyento = False
        i += 1
if nguyento:
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")
    