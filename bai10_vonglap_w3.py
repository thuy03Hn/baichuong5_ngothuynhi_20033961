# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:46:22 2024

@author: DELL _ PC
"""

import random
    dem = 0
    so_lan = 10000  # Số lần mô phỏng
    for _ in range(so_lan):
        lan_1 = 0
        for _ in range(lan_quay):
            if random.randint(1, 6) == 1:
                lan_1 += 1
        if lan_1 >= min_so_1:
            dem += 1
    return dem / so_lan

# Tính xác suất nhận ít nhất một lần số 1 khi gieo 6 lần
xac_suat_1 = xac_suat(1, 6)
print("Xác suất nhận ít nhất một lần số 1 khi gieo 6 lần:", xac_suat_1)

# Tính xác suất nhận ít nhất hai lần số 1 khi gieo 12 lần
xac_suat_2 = xac_suat(2, 12)
print("Xác suất nhận ít nhất hai lần số 1 khi gieo 12 lần:", xac_suat_2)