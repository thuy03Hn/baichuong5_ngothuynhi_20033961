# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:23:26 2024

@author: DELL _ PC
"""

n = int(input(" Nhập số nguyên dương 4 chữ số:"))
if 1000<= n <= 9999:
# Tính tổng các chữ số của N
    tong = 0
while n > 0:
    chu_so = n % 10  # Lấy chữ số cuối cùng
    tong += chu_so    # Cộng chữ số vào tổng
    n //= 10          # Bỏ chữ số cuối cùng

# In kết quả
print("Tổng các chữ số là:", tong)


