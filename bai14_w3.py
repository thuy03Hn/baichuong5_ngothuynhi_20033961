# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:26:29 2024

@author: DELL _ PC
"""

n = 1000000
tong = 0.0

for i in range(1, n + 1):
    tong += 1.0 / (i * i)

print("Tổng nghịch đảo bình phương:", tong)