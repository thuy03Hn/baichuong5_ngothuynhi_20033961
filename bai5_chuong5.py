# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:11:41 2024

@author: DELL _ PC
"""

gia_tri_hop_le = False

while not gia_tri_hop_le:
    # Nhập giá trị từ bàn phím
    nhap_vao = float(input("Nhập giá trị từ -89.9 đến 88.8: "))
    
    # Kiểm tra định dạng của chuỗi
    gia_tri_hop_le = True
    so_dau_cham = 0
    so_dau_am = 0
    ky_tu_hop_le = True
    
    i = 0
    while i < len(nhap_vao):
        ky_tu = nhap_vao[i]
        if ky_tu == '.':
            so_dau_cham += 1
        elif ky_tu == '-':
            so_dau_am += 1
        elif not ('0' <= ky_tu <= '9'):
            ky_tu_hop_le = False
        # Kiểm tra nếu có nhiều hơn một dấu chấm hoặc nhiều hơn một dấu âm
        if so_dau_cham > 1 or so_dau_am > 1:
            ky_tu_hop_le = False
        if not ky_tu_hop_le:
            gia_tri_hop_le = False
            i = len(nhap_vao)  # Kết thúc vòng lặp while
        i += 1

    if gia_tri_hop_le:
        # Chuyển đổi chuỗi thành số thực
        gia_tri = 0
        phan_thap_phan = False
        i = 0
        while i < len(nhap_vao):
            ky_tu = nhap_vao[i]
            if ky_tu == '.':
                phan_thap_phan = True
            else:
                gia_tri = gia_tri * 10 + (ord(ky_tu) - ord('0'))
                if phan_thap_phan:
                    gia_tri = gia_tri / 10
            i += 1

        # Kiểm tra giá trị có nằm trong khoảng [-89.9, 88.8] hay không
        if not (-89.9 <= gia_tri <= 88.8):
            gia_tri_hop_le = False
            print("Giá trị không nằm trong khoảng [-89.9, 88.8]. Vui lòng nhập lại.")
    else:
        print("Giá trị nhập vào không phải là số thực hợp lệ. Vui lòng nhập lại.")

print("Giá trị hợp lệ:", gia_tri)