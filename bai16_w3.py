# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:37:01 2024

@author: DELL _ PC
"""

n = int(input("Nhập một số nguyên dương n: "))

if n > 0:
   nhi_phan = ""
   while n > 0:
       nhi_phan = str(n % 2) + nhi_phan
       n = n // 2
   print("Biểu diễn nhị phân của số là:", nhi_phan)
else:
    print("Số phải là số nguyên dương.")