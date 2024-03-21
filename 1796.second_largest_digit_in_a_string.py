"""
1796. Second Largest Digit in a String
Solved
Easy
Topics
Companies
Hint
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = "0123456789"
        digits_in_s = set()
        for c in s:    
            if c in digits and c not in digits_in_s:
                digits_in_s.add(c)
        #print(digits_in_s)
        if len(digits_in_s) < 2:
            return -1
        #find highest and remove
        highest = -1
        for x in digits_in_s:
            if int(x) > int(highest):
                highest = x
        digits_in_s.remove(highest)
        #print(digits_in_s)
        #find 2nd highest
        highest = -1
        for x in digits_in_s:
            if int(x) > int(highest):
                highest = x
        return int(highest)