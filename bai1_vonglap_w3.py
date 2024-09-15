# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:40:56 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên n: "))

tim_thay = False
for a in range(1, n):
    for b in range(a + 1, n):
        for c in range(1, n):
            for d in range(c + 1, n):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    if a ** 3 + b ** 3 <= n:
                        print(f"{a}^3 + {b}^3 = {c}^3 + {d}^3")
                        tim_thay = True

if not tim_thay:
    print("Không tìm thấy số nào thỏa mãn điều kiện.")