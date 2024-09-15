# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:38:04 2024

@author: DELL _ PC
"""

n = int(input("Nhập số nguyên dương n (phải là số chẵn): "))

# Kiểm tra n phải là số chẵn
if n % 2 != 0:
    print("n phải là số chẵn. Vui lòng nhập lại.")
else:
    # Tính tổng
    s = 0
    i = 2
    while i <= n:
        s += i
        i += 2

    print("Tổng S = 2 + 4 + 6 + ... +", n, "là:", s)