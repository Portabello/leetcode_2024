"""
859. Buddy Strings
Solved
Easy
Topics
Companies
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # same strings
        if len(s) != len(goal):
            return False
        if s == goal:
            common = set()
            for x in s:
                if x in common:
                    return True
                common.add(x)
            return False
        # diff strings
        i = None
        j = None
        for x_i, x in enumerate(s):
            if x != goal[x_i] and i!=None and j!=None:
                return False
            elif x != goal[x_i] and i==None and j==None:
                i = x_i
            elif x != goal[x_i] and i!=None and j==None:
                j = x_i
        if i!=None and j!=None:
            if s[i] == goal[j] and s[j] == goal[i]:
                return True
        return False