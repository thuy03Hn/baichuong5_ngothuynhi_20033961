# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:38:22 2024

@author: DELL _ PC
"""

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n (phải là số lẻ): "))

# Kiểm tra n phải là số lẻ
if n % 2 == 0:
    print("n phải là số lẻ. Vui lòng nhập lại.")
else:
    # Tính tích
    s = 1
    i = 1
    while i <= n:
        s *= i
        i += 1

    print("Tích S = 1 * 2 * 3 * ... *", n, "là:", s)