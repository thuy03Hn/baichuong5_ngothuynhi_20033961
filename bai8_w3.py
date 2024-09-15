# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:03:06 2024

@author: DELL _ PC
"""

import random

n = int(input("Nhập số lượng số ngẫu nhiên: "))
tong = 0.0
nhonhat = float('inf')
lonnhat = float('-inf')

for _ in range(n):
    num = random.random()
    tong += num
    if num < nhonhat:
        nhonhat = num
    if num > lonnhat:
        lonnhat = num

TBC = tong / n
print("Trung bình:", TBC, "Nhỏ nhất:", nhonhat, "Lớn nhất:",lonnhat)
