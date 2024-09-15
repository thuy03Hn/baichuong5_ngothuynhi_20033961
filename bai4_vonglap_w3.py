# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:42:37 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên n: "))

dem = 0

for num in range(2, n):
    if num > 1:
        la_nguyen_to = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            dem += 1

print("Số lượng số nguyên tố nhỏ hơn", n, "là", dem)