'''
278. First Bad Version
Solved
Easy
Topics
Companies

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1



Constraints:

    1 <= bad <= n <= 231 - 1


'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        earliest_bad = None

        mid = int(n/2)
        start, end = 1, n
        while end-start > 1:
            print(start, mid,end)
            if isBadVersion(mid):
                print('loop1')
                if earliest_bad == None:
                    earliest_bad = mid
                else:
                    earliest_bad = min(earliest_bad, mid)
                end = mid
                mid = int((end+start)/2)
            else:
                print('loop2')
                start = mid
                mid = int((end+start)/2)
        print(start, mid,end)
        if isBadVersion(start):
            if earliest_bad == None:
                    earliest_bad = start
            else:
                earliest_bad = min(earliest_bad, start)
        if isBadVersion(end):
            if earliest_bad == None:
                    earliest_bad = end
            else:
                earliest_bad = min(earliest_bad, end)
        return earliest_bad
