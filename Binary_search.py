# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:48:06 2019

@author: sushil
"""

pos = -1

def search(list, n):
    
    l = 0
    u = len(list)-1
    
    while l <= u:
        mid = (l+u) // 2
        
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
                
    return False

list = [4,7,12,8,99,124,535,676,444,65475]
n = 124

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found ")
            