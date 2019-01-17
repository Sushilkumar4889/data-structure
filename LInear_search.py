# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:43:45 2019

@author: sushil
"""

pos = -1
def search(list, n):
    i = 0
    
    while i< len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
        
    return False

list = [5,8,3,6,0,2,9]
n = 9

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not FOund")