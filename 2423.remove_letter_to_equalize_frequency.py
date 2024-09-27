'''
2423. Remove Letter To Equalize Frequency
Solved
Easy
Topics
Companies
Hint

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot choose to do nothing.



Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.



Constraints:

    2 <= word.length <= 100
    word consists of lowercase English letters only.

'''
class Solution:
    def equalFrequency(self, word: str) -> bool:
        hs = {}
        for c in word:
            if c in hs:
                hs[c]+=1
            else:
                hs[c]=1
        print(hs)
        hf = {}
        for x in hs:
            if hs[x] in hf:
                hf[hs[x]]+=1
            else:
                hf[hs[x]]=1
        print(hf)
        if (len(hf) == 1):
            return list(hf.keys())[0] == 1 or list(hf.values())[0] == 1
        if (len(hf) == 2):
            f1, f2 = min(hf.keys()), max(hf.keys())
            return (f1 + 1 == f2 and hf[f2] == 1) or (f1 == 1 and hf[f1] == 1)
        return False
