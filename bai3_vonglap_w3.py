# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:41:46 2024

@author: DELL _ PC
"""

so = input("Nhập số ISBN 9 chữ số: ")

if len(so) == 9 and so.isdigit():
    tong = 0
    for i in range(9):
        tong += (10 - i) * int(so[i])
    
    chu_so_kiem_tra = 11 - (tong % 11)
    if chu_so_kiem_tra == 10:
        chu_so_kiem_tra = 'X'
    elif chu_so_kiem_tra == 11:
        chu_so_kiem_tra = 0
    print(f"Số ISBN đầy đủ là: {so}{chu_so_kiem_tra}")
else:
    print("Số ISBN không hợp lệ")