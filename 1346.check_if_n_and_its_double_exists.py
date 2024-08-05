'''
1346. Check If N and Its Double Exist
Solved
Easy
Topics
Companies
Hint
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        t = set()
        for x in arr:
            if x in t and x==0:
                return True
            if x not in t:
                t.add(x)
        #print(arr)
        for x in arr:
            if x*2 in t and x!=0:
                print('found', x)
                return True
        return False
