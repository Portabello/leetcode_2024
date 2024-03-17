"""
1768. Merge Strings Alternately
Solved
Easy
Topics
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t = 0
        ans = ""
        while word1 or word2:
            if t==0 and len(word1)!= 0:
                t=1
                ans = ans + word1[0]
                word1 = word1[1:]
            
            elif t==1 and len(word2)!= 0:
                t=0
                ans = ans + word2[0]
                word2 = word2[1:]
            else:
                if len(word1) != 0:
                    ans = ans + word1
                    word1 = ""
                if len(word2) != 0:
                    ans = ans + word2
                    word2 = ""
        print(ans)
        return ans