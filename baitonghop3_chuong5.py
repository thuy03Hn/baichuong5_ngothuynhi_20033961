# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:21:08 2024

@author: DELL _ PC
"""
# ID User cần kiểm tra
id_user = "exampleID"  # Thay thế bằng ID user cần kiểm tra
# Mật khẩu cần kiểm tra
password = "Example@123"  # Thay thế bằng mật khẩu cần kiểm tra

# Danh sách các ký tự không hợp lệ cho ID user
ky_tu_khong_hop_le = "!@#$%^&*()-=+"

# Kiểm tra ID User
# Đếm số ký tự trong id_user
dem_id_user = 0
for char in id_user:
    dem_id_user += 1

# Kiểm tra điều kiện của ID user
if dem_id_user < 6 or dem_id_user > 24:
    print("ID user không hợp lệ: Chiều dài phải từ 6 đến 24 ký tự.")
else:
    # Kiểm tra ký tự không hợp lệ và khoảng trắng trong ID user
    id_user_hop_le = True
    for char in id_user:
        if char in ky_tu_khong_hop_le or char.isspace():
            id_user_hop_le = False
            break

    if id_user_hop_le:
        print("ID user hợp lệ.")
    else:
        print("ID user không hợp lệ: Không chứa ký tự đặc biệt và khoảng trắng.")

# Kiểm tra Password
# Đếm số ký tự trong password
dem_password = 0
for char in password:
    dem_password += 1

# Kiểm tra điều kiện của mật khẩu
if dem_password < 6 or dem_password > 24:
    print("Mật khẩu không hợp lệ: Chiều dài phải từ 6 đến 24 ký tự.")
else:
    # Kiểm tra các yêu cầu của mật khẩu
    co_chu_thuong = False
    co_so = False
    co_chu_hoa = False
    co_ky_tu_dac_biet = False

    for char in password:
        if char.islower():
            co_chu_thuong = True
        elif char.isdigit():
            co_so = True
        elif char.isupper():
            co_chu_hoa = True
        elif char in "$#@":
            co_ky_tu_dac_biet = True

    if co_chu_thuong and co_so and co_chu_hoa and co_ky_tu_dac_biet:
        print("Mật khẩu hợp lệ.")
    else:
        print("Mật khẩu không hợp lệ: Cần chứa ít nhất 1 chữ cái thường, 1 chữ cái hoa, 1 số, và 1 ký tự đặc biệt trong [$#@].")