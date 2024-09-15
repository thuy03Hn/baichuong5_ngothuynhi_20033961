# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:46:41 2024

@author: DELL _ PC
"""

muc_tieu = 979

# Khởi tạo biến để lưu bộ nghiệm có tổng x + y + z nhỏ nhất
tong_min = float('inf')
bo_nghiem_tot_nhat = None

# Liệt kê tất cả bộ nghiệm nguyên và tìm bộ nghiệm có tổng nhỏ nhất
x = 1
while 2 * x < muc_tieu:
    y = 1
    while 2 * x + 7 * y < muc_tieu:
        z = 1
        while 2 * x + 7 * y + 9 * z <= muc_tieu:
            if 2 * x + 7 * y + 9 * z == muc_tieu:
                tong_hien_tai = x + y + z
                if tong_hien_tai < tong_min:
                    tong_min = tong_hien_tai
                    bo_nghiem_tot_nhat = (x, y, z)
            z += 1
        y += 1
    x += 1

if bo_nghiem_tot_nhat:
    print("Bộ nghiệm có tổng x + y + z nhỏ nhất là:")
    print("x =", bo_nghiem_tot_nhat[0], ", y =", bo_nghiem_tot_nhat[1], ", z =", bo_nghiem_tot_nhat[2])
else:
    print("Không có bộ nghiệm nào.")