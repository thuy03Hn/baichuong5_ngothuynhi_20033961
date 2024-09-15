# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:54:51 2024

@author: DELL _ PC
"""

import time

# Thiết lập danh sách các lựa chọn
lua_chon = ["Kéo", "Búa", "Bao"]

# Người chơi nhập vào lựa chọn
lua_chon_nguoi = input("Nhập Kéo, Búa hoặc Bao: ")

# Kiểm tra nhập có hợp lệ không
lua_chon_nguoi = lua_chon_nguoi.capitalize()  # Viết hoa chữ cái đầu
if lua_chon_nguoi not in lua_chon:
    print("Lựa chọn không hợp lệ.")
else:
    # Máy chọn ngẫu nhiên bằng cách sử dụng thời gian làm chỉ số ngẫu nhiên
    # Đếm số giây hiện tại và dùng để chọn ngẫu nhiên một trong ba
    thoi_gian = int(time.time())
    chi_so_may = thoi_gian % 3
    lua_chon_may = lua_chon[chi_so_may]

    print("Máy chọn:", lua_chon_may)

    # Kiểm tra kết quả
    if lua_chon_nguoi == lua_chon_may:
        print("Hòa!")
    elif (lua_chon_nguoi == "Kéo" and lua_chon_may == "Bao") or \
         (lua_chon_nguoi == "Búa" and lua_chon_may == "Kéo") or \
         (lua_chon_nguoi == "Bao" and lua_chon_may == "Búa"):
        print("Bạn thắng!")
    else:
        print("Bạn thua!")