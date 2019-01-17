# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:03:35 2019

@author: sushil
"""

def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if(len(lst) == 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

arr = [1,2,-1,0,9,62,7,2,3,1,43,143]
print(mergesort(arr))