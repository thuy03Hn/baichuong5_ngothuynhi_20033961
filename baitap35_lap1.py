# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:37:28 2024

@author: DELL _ PC
"""

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tính tổng
s = 0
i = 1
while i <= n:
    s += i
    i += 1

print("Tổng S = 1 + 2 + 3 + ... +", n, "là:", s)