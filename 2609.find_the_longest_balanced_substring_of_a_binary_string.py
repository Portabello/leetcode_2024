'''
2609. Find the Longest Balanced Substring of a Binary String
Solved
Easy
Topics
Companies
Hint

You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.

Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4.

Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.



Constraints:

    1 <= s.length <= 50
    '0' <= s[i] <= '1'

'''
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_subsequence = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.isValidBalancedSubstring(s[i:j]):
                    max_subsequence = max(max_subsequence, len(s[i:j]))
        return max_subsequence

    def isValidBalancedSubstring(self, s):
        if len(s)%2!=0:
            return False
        zero_count = 0
        one_count = 0
        flag = False
        for c in s:
            if c=='0':
                if flag:
                    return False
                zero_count +=1
            if c=='1':
                flag = True
                one_count += 1
        if zero_count != one_count:
            return False
        return True
            
