# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:48:54 2024

@author: DELL _ PC
"""
gioi_han = int(input("Nhập giá trị giới hạn: "))

# Duyệt qua tất cả các tổ hợp có thể
for a in range(1, gioi_han):
    for b in range(a, gioi_han):
        for c in range(b, gioi_han):
            for d in range(c, gioi_han):
                for e in range(d + 1, gioi_han):
                    # Tính tổng lũy thừa của 5
                    tong_luy_thua = a**5 + b**5 + c**5 + d**5
                    luy_thua_e = e**5
                    if tong_luy_thua == luy_thua_e:
                        print(f"{a}^5 + {b}^5 + {c}^5 + {d}^5 = {e}^5")