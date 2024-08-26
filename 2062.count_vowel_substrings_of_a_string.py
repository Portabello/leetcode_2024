'''
2062. Count Vowel Substrings of a String
Solved
Easy
Topics
Companies
Hint

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"



Constraints:

    1 <= word.length <= 100
    word consists of lowercase English letters only.


'''
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word)<5:
            return 0
        ans = 0
        constanants = 'bcdfghjklmnpqrstvwxyz'
        for i in range(0,len(word)-4):
            for j in range(5,len(word)-i+1):
                #if j > len(word)-1:
                #    break
                t = word[i:i+j]
                if 'a' in t and 'e' in t and 'i' in t and 'o' in t and 'u' in t:
                    valid = True
                    for x in t:
                        if x in constanants:
                            #print(x)
                            valid = False
                    if valid:
                        ans += 1
                    #print(t,valid)
                #print(i,i+j,word[i:i+j])
        return ans
