# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:29:16 2024

@author: DELL _ PC
"""

a = 0
b = 0
c = 0

while not (a > 0 and b > 0 and c > 0):
    a = int(input("Nhập số nguyên dương a: "))
    b = int(input("Nhập số nguyên dương b: "))
    c = int(input("Nhập số nguyên dương c: "))
    if not (a > 0 and b > 0 and c > 0):
        print("Tất cả các số phải là số nguyên dương. Vui lòng nhập lại.")

# Sắp xếp ba cạnh để kiểm tra điều kiện tam giác dễ hơn
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Kiểm tra điều kiện tam giác
if a + b > c:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Ba số tạo thành một tam giác đều.")
    elif a == b or b == c or a == c:
        # Kiểm tra tam giác vuông
        if a**2 + b**2 == c**2:
            print("Ba số tạo thành một tam giác cân và vuông.")
        else:
            print("Ba số tạo thành một tam giác cân.")
    elif a**2 + b**2 == c**2:
        print("Ba số tạo thành một tam giác vuông.")
    else:
        print("Ba số tạo thành một tam giác thường.")
else:
    print("Ba số không thể tạo thành một tam giác.")