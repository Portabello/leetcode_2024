"""
187. Repeated DNA Sequences
Solved
Medium
Topics
Companies
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hs = {}
        for i in range(len(s)-9):
            #print(s[i:i+10])
            if s[i:i+10] in hs:
                hs[s[i:i+10]]+=1
            else:
                hs[s[i:i+10]]=1
        ans = []
        for x in hs:
            if hs[x]>1:
                ans.append(x)
        return ans
