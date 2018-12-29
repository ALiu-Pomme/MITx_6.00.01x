# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:13:26 2018

@author: Amanda
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    sorted_keys = []
    values = []
    for value in aDict.values():
        values.append(value)
    for key in aDict.keys():
        if values.count(aDict[key]) == 1:
            sorted_keys.append(key)
    sorted_keys.sort()
    return sorted_keys

a = {1: 1, 3: 1, 2:1}
print(uniqueValues(a))