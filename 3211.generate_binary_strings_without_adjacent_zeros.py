'''
3211. Generate Binary Strings Without Adjacent Zeros
Solved
Medium
Topics
Companies
Hint

You are given a positive integer n.

A binary string x is valid if all
substrings
of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.



Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".



Constraints:

    1 <= n <= 18

'''
class Solution:
    def validStrings(self, n: int) -> List[str]:

        def rc(n, ans):
            new_ans = []
            for entry in ans:
                #if ends in 0
                if entry[-1] == '0':
                    new_ans.append(entry+'1')
                #if ends in 1
                elif entry[-1] == '1':
                    new_ans.append(entry+'0')
                    new_ans.append(entry+'1')
            return new_ans

        #base case n==1
        ans = ['0','1']
        for x in range(1,n):
            ans = rc(x, ans)
        return ans
