# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:08:15 2024

@author: DELL _ PC
"""

dayso = [2, 4, 8, 16, 32, 64, 128]

print("n\tlog(n)\tn*log(n)\tn^2\t\tn^3")
for n in dayso:
    log_n = 0
    k = n
    while k > 1:
        k //= 2
        log_n += 1
    n_log_n = n * log_n
    n_binhphuong = n ** 2
    n_lapphuong = n ** 3
    print(n, '\t', log_n, '\t', n_log_n, '\t', n_binhphuong, '\t', n_lapphuong)
    