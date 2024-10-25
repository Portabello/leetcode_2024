'''
131. Palindrome Partitioning
Solved
Medium
Topics
Companies

Given a string s, partition s such that every
substring
of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]



Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        def bt(s, r):
            if len(s)==0:
                res.append(r)
                return
            for l in range(1,len(s)+1):
                t = s[0:l]
                #print(l,t)
                if t == t[::-1]:
                    new_r = r + [t]
                    bt(s[l:], new_r)
        bt(s, [])
        return res
