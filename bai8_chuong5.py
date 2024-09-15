# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:46:00 2024

@author: DELL _ PC
"""

n = int(input("Nhập giá trị nguyên n: "))
ket_qua = {}
for i in range(1, n + 1):
    ket_qua[i] = i ** i
print(ket_qua)
