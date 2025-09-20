'''
819. Most Common Word
Solved
Easy
Topics
Companies
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.



Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"


Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hs = {}
        cur_word = ""
        words = []
        for c in paragraph:
            if c.isalpha():
                cur_word = cur_word + c.lower()
            else:
                if cur_word not in banned and cur_word!="":
                    words.append(cur_word)
                cur_word = ""
        if cur_word not in banned:
            words.append(cur_word)
        print(words)
        for word in words:
            if word in hs:
                hs[word]+=1
            else:
                hs[word]=1
        max_frequency, max_word =0, -1
        for x in hs:
            if hs[x]>max_frequency:
                max_frequency=hs[x]
                max_word = x
        return max_word
