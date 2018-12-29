# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:22:05 2018

@author: Amanda
"""
def laceStrings (s1, s2):
    merged = ''
    if s1 >= s2:
        for num in range(len(s1)):
            merged += s1[num]
            try:
                merged += s2[num]
            except IndexError:
                pass
    else:
        for num in range(len(s2)):
            try:
                merged += s1[num]
            except IndexError:
                pass
            merged += s2[num]
    return merged


print(laceStrings('[ as', 's0;)'))