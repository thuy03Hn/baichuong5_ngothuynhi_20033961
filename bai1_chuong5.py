# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:30:49 2024

@author: DELL _ PC
"""

n = int(input("Nhập số n từ bàn phím:"))
giaithua = 1
for i in range(1,n+1):
 giaithua *= i
print("Tính ra",n,"giai thừa",giaithua)
