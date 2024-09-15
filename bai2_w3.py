# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:59:02 2024

@author: DELL _ PC
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    # Phương trình bậc nhất
    if b != 0:
        x = -c / b
        print(f"Nghiệm là: {x}")
    else:
        print("Phương trình vô nghiệm")
else:
    # Phương trình bậc hai
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("Có 2 nghiệm phân biệt:", x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("Có nghiệm kép:" x)
    else:
        print("Phương trình vô nghiệm")