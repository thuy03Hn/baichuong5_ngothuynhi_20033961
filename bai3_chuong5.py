# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:59:12 2024

@author: DELL _ PC
"""

import random
so_phan_tu = random.randrange(20, 31) # ngẫu nhiên từ 20 đến 30
danh_sach_binh_phuong = [0] * so_phan_tu  
for i in range(so_phan_tu):
    so_ngau_nhien = random.randrange(18, 100)  #  18 đến 99
    binh_phuong = so_ngau_nhien * so_ngau_nhien  # Tính bình phương
    danh_sach_binh_phuong[i] = binh_phuong  
print("Số lượng phần tử:", so_phan_tu)
print("Danh sách các giá trị bình phương:")
for gia_tri in danh_sach_binh_phuong:
    print(gia_tri)
    