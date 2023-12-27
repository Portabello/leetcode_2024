"""
290. Word Pattern
Easy
7K
907
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_table = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for i,x in enumerate(pattern):
            print(x, s_list[i])
            if x in hash_table:
                #check if its the same
                if(hash_table[x] != s_list[i]):
                    return False
            else:
                #make sure its not duplicate
                if s_list[i] in hash_table.values():
                    return False
                hash_table[x] = s_list[i]
        return True