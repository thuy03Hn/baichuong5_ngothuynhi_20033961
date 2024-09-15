# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:46:47 2024

@author: DELL _ PC
"""
import random

# Nhập số lần mô phỏng trò chơi
so_lan = int(input("Nhập số lần mô phỏng trò chơi: "))

# Biến để đếm số lần thắng
thang_khong_chuyen = 0
thang_chuyen = 0

# Mô phỏng không đổi cửa
for _ in range(so_lan):
    cua_choi = random.randint(1, 3)
    cua_giai_thuong = random.randint(1, 3)
    cua_mo = 6 - cua_choi - cua_giai_thuong
    if cua_choi == cua_giai_thuong:
        thang_khong_chuyen += 1

# Mô phỏng đổi cửa
for _ in range(so_lan):
    cua_choi = random.randint(1, 3)
    cua_giai_thuong = random.randint(1, 3)
    cua_mo = 6 - cua_choi - cua_giai_thuong
    cua_choi = 6 - cua_choi - cua_mo
    if cua_choi == cua_giai_thuong:
        thang_chuyen += 1

# Tính xác suất
xac_suat_khong_chuyen = thang_khong_chuyen / so_lan
xac_suat_chuyen = thang_chuyen / so_lan

# In kết quả
print("Xác suất thắng khi không đổi cửa:", xac_suat_khong_chuyen)
print("Xác suất thắng khi đổi cửa:", xac_suat_chuyen)