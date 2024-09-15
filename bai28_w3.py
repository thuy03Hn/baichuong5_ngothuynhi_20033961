# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:38:55 2024

@author: DELL _ PC
"""

x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))

while y != 0:
    x, y = y, x % y

print("Ước chung lớn nhất của", x, "và", y, "là:", x)