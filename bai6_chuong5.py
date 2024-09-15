# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:37:16 2024

@author: DELL _ PC
"""

# tạo danh sách các số chẵn và chia hết cho 5 từ 2018 đến 2828
kich_thuoc_toi_da = (2828 - 2018) // 10 + 1
so = [0] * kich_thuoc_toi_da
a = 0

bat_dau = 2018
ket_thuc = 2828
i = bat_dau

while i <= ket_thuc:
    if i % 2 == 0 and i % 5 == 0:
        if a < kich_thuoc_toi_da:  # Đảm bảo không vượt quá kích thước danh sách
            so[a] = i
            a += 1
    i += 1

# Bước 2: In các số thành chuỗi, cách nhau bằng 1 tab
i = 0
while i < kich_thuoc_toi_da and so[i] != 0:  # Kiểm tra các số khác 0
    print(so[i], end='')
    if i < kich_thuoc_toi_da - 1 and so[i + 1] != 0:  # Nếu không phải số cuối cùng
        print('\t', end='')  # In tab giữa các số
    i += 1