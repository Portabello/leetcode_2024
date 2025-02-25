'''
696. Count Binary Substrings
Attempted
Easy
Topics
Companies
Hint

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.



Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.



Constraints:

    1 <= s.length <= 105
    s[i] is either '0' or '1'.

'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = 2
        ans = 0
        while l <= len(s):

            for i in range(0, len(s)-l+1):
                subs = s[i:i+l]
                valid = True
                #print(subs[0:int(len(subs)/2)], '    /     ',subs[int(len(subs)/2):])
                if subs[0] == '0':
                    if subs[0:int(len(subs)/2)] == '0'*(int(len(subs)/2)) and subs[int(len(subs)/2):] == '1'*(int(len(subs)/2)):
                        #print('valid')
                        ans += 1
                else:
                    if subs[0:int(len(subs)/2)] == '1'*(int(len(subs)/2)) and subs[int(len(subs)/2):] == '0'*(int(len(subs)/2)):
                        #print('valid')
                        ans += 1
            l += 2
        return ans
