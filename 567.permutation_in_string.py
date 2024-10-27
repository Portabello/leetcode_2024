'''
567. Permutation in String
Solved
Medium
Topics
Companies
Hint

Given two strings s1 and s2, return true if s2 contains a
permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false



Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for c in s1:
            if c in s1_freq:
                s1_freq[c] += 1
            else:
                s1_freq[c] = 1
        s2_freq = {}
        s1_len = len(s1)
        for i in range(len(s2)-len(s1)+1):
            #print(s2[i:i+s1_len])
            if len(s2_freq) == 0:
                for x in s2[i:i+s1_len]:
                    if x in s2_freq:
                        s2_freq[x] += 1
                    else:
                        s2_freq[x] = 1
            else:
                s2_freq[s2[i-1]] -= 1
                if s2_freq[s2[i-1]] == 0:
                    del s2_freq[s2[i-1]]
                new = s2[i+s1_len-1]
                if new in s2_freq:
                    s2_freq[new] += 1
                else:
                    s2_freq[new] = 1
            #print(s2_freq)
            if s1_freq == s2_freq:
                return True
        return False
