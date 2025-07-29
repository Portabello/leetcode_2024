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
        row1, row2, row3 = ["qwertyuiop"], ["asdfghjkl"], ["zxcvbnm"]
        hs = {}
        row=1
        for x in row1+row2+row3:
            for y in x:
                hs[y] = row
            row +=1
        ans = []
        for word in words:
            valid = True
            og=word
            word = word.lower()
            row = hs[word[0]]
            for char in word:
                if hs[char] != row:
                    valid = False
            if valid:
                ans.append(og)
        return ans
