"""
1002. Find Common Characters
Solved
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        for i,x in enumerate(words):
            if i==0:
                for c in x:
                    if c in common:
                        common[c]+=1
                    else:
                        common[c]=1
            else:
                tmp = {}
                for c in x:
                    if c in common:
                        if common[c]>0:
                            common[c] -= 1
                            if c in tmp:
                                tmp[c]+=1
                            else:
                                tmp[c]=1
                common = tmp
        ans = []
        for x in common:
            ans = ans + [x]*common[x]
        return ans
