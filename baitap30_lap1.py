# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:28:10 2024

@author: DELL _ PC
"""

thang = 0
nam = 0

while not (1 <= thang <= 12 and nam > 0):
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))
    if not (1 <= thang <= 12 and nam > 0):
        print("Tháng phải từ 1 đến 12 và năm phải là số nguyên dương. Vui lòng nhập lại.")

# Kiểm tra năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    nam_nhuan = True
else:
    nam_nhuan = False

# Xác định số ngày trong tháng
if thang == 2:
    if nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:
    so_ngay = 31

# In kết quả
print("Tháng", thang, "năm", nam, "có", so_ngay, "ngày.")