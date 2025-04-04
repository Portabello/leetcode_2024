'''
3120. Count the Number of Special Characters I
Solved
Easy
Topics
Companies
Hint

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.



Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.



Constraints:

    1 <= word.length <= 50
    word consists of only lowercase and uppercase English letters.

'''
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        for x in word:
            if x.islower():
                lower[x] = 1
        ans = 0
        for x in word:
            if x.isupper() and x.lower() in lower:
                ans += 1
                del lower[x.lower()]
        return ans
