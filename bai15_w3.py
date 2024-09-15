# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:35:12 2024

@author: DELL _ PC
"""

i = int(input("Nhập số nguyên i: "))
k = int(input("Nhập cơ số k (từ 2 đến 16): "))

if 2 <= k <= 16:
    kytu = "0123456789ABCDEF"
    ketqua = ""
    while i > 0:
        du = i % k
        ketqua = kytu[du] + ketqua
        i = i // k
    print("Biểu diễn cơ số", k, "của số là:", ketqua)
else:
    print("Cơ số không hợp lệ. Vui lòng nhập cơ số từ 2 đến 16.")