'''
941. Valid Mountain Array
Solved
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        max_arr = max(arr)
        max_i = arr.index(max_arr)
        #print(max_i, max_arr)
        if max_i == 0 or max_i == len(arr)-1:
            return False
        for i,x in enumerate(arr):
            if i<max_i:
                #print('loop1', arr[i], arr[i+1])
                if arr[i]>=arr[i+1]:
                    #print('false')
                    return False
            if i>max_i:
                #print('loop2', arr[i], arr[i-1])
                if arr[i]>=arr[i-1]:
                    #print('false')
                    return False
        return True
