# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:09:22 2024

@author: DELL _ PC
"""

giatrihople = False
while not giatrihople:
    giatri = float(input("Nhập giá trị từ -99 đến 99: "))
    if -99 <= giatri <= 99:# Kiểm tra có nằm trong khoảng [-99, 99] hay không
        giatrihople = True  # Đặt biến kiểm soát là True để thoát khỏi vòng lặp
    else:
        print("Giá trị không nằm trong khoảng [-99, 99]. Vui lòng nhập lại.")

print("Giá trị hợp lệ:", giatri)