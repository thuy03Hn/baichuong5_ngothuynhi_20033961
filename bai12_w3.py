# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:25:12 2024

@author: DELL _ PC
"""

a, b = 0, 1
for _ in range(100):
    print(a, end=' ')
    a, b = b, a + b
print()
