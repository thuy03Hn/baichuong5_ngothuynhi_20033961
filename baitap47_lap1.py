# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:42:58 2024

@author: DELL _ PC
"""

# Khai báo phương trình và số cần tìm
muctieu = 979

# Khởi tạo biến để lưu bộ nghiệm có tổng x + y + z lớn nhất
tong = 0
nghiem = []

# Liệt kê tất cả bộ nghiệm nguyên và tìm bộ nghiệm có tổng lớn nhất
x = 1
while 2 * x < muctieu:
    y = 1
    while 2 * x + 7 * y < muctieu:
        z = 1
        while 2 * x + 7 * y + 9 * z <= muctieu:
            if 2 * x + 7 * y + 9 * z == muctieu:
                tonghientai = x + y + z
                if tonghientai > tong:
                    tong = tonghientai
                    nghiem = (x, y, z)
            z += 1
        y += 1
    x += 1


if nghiem:
    print("Bộ nghiệm có tổng x + y + z lớn nhất là:")
    print(f"x = {nghiem[0]}, y = {nghiem[1]}, z = {nghiem[2]}")
else:
    print("Không có bộ nghiệm nào.")
    