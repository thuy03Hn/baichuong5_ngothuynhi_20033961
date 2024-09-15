# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:39:16 2024

@author: DELL _ PC
"""

sochan = 0
sole = 0

for i in range(101):
    if i % 2 == 0:
        sochan += i
    else:
        sole += i

print("Tổng của tất cả các số chẵn từ 0 đến 100:", sochan)
print("Tổng của tất cả các số lẻ từ 0 đến 100:", sole)