# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:24:57 2024

@author: DELL _ PC
"""

n = 123456789
m = 0

while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10

print("M:", m)