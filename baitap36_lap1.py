# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:37:54 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên dương n: "))

# Tính tổng
s = 0
i = 1
while i <= n:
    s += i * i
    i += 1

print("Tổng S = 1^2 + 2^2 + 3^2 + ... +", n, "^2 là:", s)