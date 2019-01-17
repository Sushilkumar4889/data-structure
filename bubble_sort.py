# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:55:57 2019

@author: sushil
"""

def sort(num):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
            
nums = [5,3,6,9,1,0,]
sort(nums)

print(nums)