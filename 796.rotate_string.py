'''
796. Rotate String
Solved
Easy
Topics
Companies

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.



Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false



Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.

'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if Counter(s) != Counter(goal) or len(s) != len(goal):
            return False
        for i,x in enumerate(goal):
            if x == s[0]:
                if (goal[i:] + goal[0:i]) == s:
                    return True
        return False
