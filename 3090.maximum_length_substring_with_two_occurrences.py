'''
3090. Maximum Length Substring With Two Occurrences
Solved
Easy
Topics
Companies
Hint
Given a string s, return the maximum length of a
 such that it contains at most two occurrences of each character.



Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".



Constraints:

    2 <= s.length <= 100
    s consists only of lowercase English letters.
'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        def valid_string(s1):
            freq = {}
            for c in s1:
                if c in freq:
                    freq[c]+=1
                    if freq[c]>2:
                        return False
                else:
                    freq[c]=1
            return True
        max_str = None
        for l in range(1,len(s)+1):
            #print(l)
            for i in range(0,len(s)-l+1):
                print(s[i:i+l])
                substring = s[i:i+l]
                if valid_string(substring):
                    print(substring, 'is valid')
                    max_str = substring
        return len(max_str)
