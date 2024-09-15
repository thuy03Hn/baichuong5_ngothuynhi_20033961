# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:42:12 2024

@author: DELL _ PC
"""

muctieu = 979
# Liệt kê tất cả bộ nghiệm nguyên
print("Các bộ nghiệm nguyên của phương trình 2x + 7y + 9z = 979 với x, y, z > 0 là:")
x = 1
while 2 * x < muctieu:
    y = 1
    while 2 * x + 7 * y < muctieu:
        z = 1
        while 2 * x + 7 * y + 9 * z <= muctieu:
            if 2 * x + 7 * y + 9 * z == muctieu:
                print(f"x = {x}, y = {y}, z = {z}")
            z += 1
        y += 1
    x += 1