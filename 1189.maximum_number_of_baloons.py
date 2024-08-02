'''
1189. Maximum Number of Balloons
Solved
Easy
Topics
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_d = {}
        for c in text:
            if c in text_d:
                text_d[c] += 1
            else:
                text_d[c] = 1
        count = 0
        valid = True
        while True:
            for c in 'balloon':
                if c in text_d:
                    if text_d[c]!=0:
                        text_d[c]-=1
                    else:
                        valid=False
                        break
                else:
                    valid=False
                    break
            if valid:
                count +=1
            if valid == False:
                break
        return count
                        
