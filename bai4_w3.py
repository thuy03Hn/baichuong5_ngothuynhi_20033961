# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:00:23 2024

@author: DELL _ PC
"""

nhietdo = float(input("Nhập nhiệt độ (<= 0): "))
gio = float(input("Nhập tốc độ gió (>= 3): "))

if nhietdo <= 0 and gio >= 3:
    wind_chill = 35.74 + 0.6215 * nhietdo - 35.75 * (gio ** 0.16) + 0.4275 * nhietdo * (gio ** 0.16)
    print("Wind Chill Index:",wind_chill)
else:
    print("Giá trị không hợp lệ. Nhiệt độ phải <= 0 và tốc độ gió >= 3.")