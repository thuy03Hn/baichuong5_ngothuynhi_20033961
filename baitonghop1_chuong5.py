# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:47:53 2024

@author: DELL _ PC
"""

a = input("Nhập chuỗi: ")

# Tính độ dài chuỗi
do_dai = 0
for _ in a:
    do_dai += 1

print(f"Độ dài chuỗi: {do_dai}")

# Đếm các ký tự đặc biệt
ky_tu_dac_biet = "!@#$%^&*()-=+./"
dem_dac_biet = 0
for ky_tu in a:
    if ky_tu in ky_tu_dac_biet:
        dem_dac_biet += 1

print(f"Số ký tự đặc biệt: {dem_dac_biet}")

# Đếm các ký tự chữ cái từ a-z
dem_chu_cai_thuong = 0
for ky_tu in a:
    if 'a' <= ky_tu <= 'z':
        dem_chu_cai_thuong += 1

print(f"Số ký tự chữ cái thường: {dem_chu_cai_thuong}")

# Đếm các ký tự chữ số từ 0-9
dem_chu_so = 0
for ky_tu in a:
    if '0' <= ky_tu <= '9':
        dem_chu_so += 1

print(f"Số ký tự chữ số: {dem_chu_so}")

# Đếm các ký tự chữ cái hoa từ A-Z
dem_chu_cai_hoa = 0
for ky_tu in a:
    if 'A' <= ky_tu <= 'Z':
        dem_chu_cai_hoa += 1

print(f"Số ký tự chữ cái hoa: {dem_chu_cai_hoa}")
