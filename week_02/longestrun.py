# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:47:27 2018

@author: Amanda
"""

def longestRun(L):
    count = 1
    longest = 1
    for num in range(1, len(L)):
        if L[num] >= L[num-1]:
            count += 1
            if count > longest:
                longest = count
        else:
            if count > longest:
                longest = count
            count = 1        
    return longest


L = [10, 4, 6, 8, -3, 5, 7, 7, 2]
print(longestRun([14, 16, 18, 20, 8, 10, 12, 4, 6, 2]))