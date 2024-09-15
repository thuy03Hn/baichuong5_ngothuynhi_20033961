# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:44:31 2024

@author: DELL _ PC
"""

n = 87539319

tim_thay = False

for a in range(1, int(n**(1/3)) + 1):
    for b in range(a + 1, int(n**(1/3)) + 1):
        for c in range(1, int(n**(1/3)) + 1):
            for d in range(c + 1, int(n**(1/3)) + 1):
                if a**3 + b**3 == c**3 + d**3:
                    if a**3 + b**3 == n:
                        print(str(a) + "^3 + " + str(b) + "^3 = " + str(c) + "^3 + " + str(d) + "^3")
                        tim_thay = True

if not tim_thay:
    print("Không tìm thấy số nào thỏa mãn điều kiện.")