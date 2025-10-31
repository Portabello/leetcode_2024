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
        ans = []
        def recurse(cur_partition, remaining):
            #print(cur_partition, remaining)
            if len(remaining)==0:
                ans.append(cur_partition)
                return
            for i in range(1, len(remaining)+1):
                substring = remaining[0:i]
                #print('checking substring ', substring)
                if substring==substring[::-1]:
                    recurse(cur_partition+[substring], remaining[i:])
        recurse([], s)
        #print('ans', ans)
        return ans
