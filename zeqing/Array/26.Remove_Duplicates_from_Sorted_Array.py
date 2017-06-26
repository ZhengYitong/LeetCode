# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        new_length = 0
        for i in range(1, length):
        	if nums[i] != nums[new_length]:
        		new_length += 1
        		nums[new_length] = nums[i]
        return new_length + 1