'''
520. Detect Capital
Solved
Easy
Topics
Companies
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false


Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_capital = True if word[0].isupper() else False
        num_capital = 0
        for c in word:
            if c.isupper():
                num_capital += 1
        if (num_capital==1 and first_capital) or num_capital==len(word) or num_capital==0:
            return True
        return False
