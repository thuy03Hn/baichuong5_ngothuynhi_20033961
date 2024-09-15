# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:30:46 2024

@author: DELL _ PC
"""

km = int(input("Nhập số km đã đi: "))

# Tính tiền cước
tong_tien = 0

if km > 0:
    #  km đầu tiên
    tong_tien += 15000
    km -= 1

    #  km thứ 2 đến thứ 5
    if km > 0:
        if km > 4:
            tong_tien += 13500 * 4
            km -= 4
        else:
            tong_tien += 13500 * km
            km = 0

    #  km thứ 6 trở đi
    if km > 0:
        tong_tien += 11000 * km

    if km + 5 > 120:
        tong_tien *= 0.9

    print("Tổng tiền cước TAXI là:", tong_tien, "đồng.")
else:
    print("Số km phải là số nguyên dương.")