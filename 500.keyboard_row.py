'''
500. Keyboard Row
Solved
Easy
Topics
Companies

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".



Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]



Constraints:

    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] consists of English letters (both lowercase and uppercase).


'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []
        for word in words:
            if word[0].lower() in row1:
                if self.isInRow(word,row1):
                    ans.append(word)
            elif word[0].lower() in row2:
                if self.isInRow(word,row2):
                    ans.append(word)
            else:
                if self.isInRow(word,row3):
                    ans.append(word)
        return ans

    def isInRow(self, word, row):
        for c in word:
            if c.lower() not in row:
                return False
        return True
