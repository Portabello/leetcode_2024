'''
541. Reverse String II
Solved
Easy
Topics
Companies
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.



Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), 2*k):
            chars_left = len(s)-i
            #print(chars_left)
            #fewer than k chars left
            if(chars_left < k):
                #print('loop1')
                ans = ans + s[i:][::-1]
            #less than 2k chars left but >= k chars
            elif(chars_left < 2*k and chars_left >= k):
                #print('loop2')
                #print(s[i:i+k][::-1] , s[i+k:])
                ans = ans + s[i:i+k][::-1] + s[i+k:]
            #base case
            else:
                #print('loop3')
                ans = ans + s[i:i+k][::-1] + s[i+k:i+2*k]
            #print(ans)
        return ans
