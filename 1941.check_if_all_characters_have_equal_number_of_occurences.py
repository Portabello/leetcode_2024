'''
1941. Check if All Characters Have Equal Number of Occurrences
Solved
Easy
Topics
Companies
Hint
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency_hash = {}
        for char in s:
            if char in frequency_hash:
                frequency_hash[char] += 1
            else:
                frequency_hash[char] = 1

        good_frequency = None
        for char in frequency_hash:
            if good_frequency == None:
                good_frequency = frequency_hash[char]
            if good_frequency != frequency_hash[char]:
                return False
        return True
