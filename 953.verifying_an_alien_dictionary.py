'''
953. Verifying an Alien Dictionary
Solved
Easy
Topics
Companies
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1:
            return True
        prev = words[0]
        for i in range(1, len(words)):
            #compare word to prev
            word = words[i]
            min_len = min(len(word), len(prev))
            for j in range(0, min_len):
                print(prev[j],order.index(prev[j])," - ",word[j],order.index(word[j]))
                if prev[j]!=word[j]:
                    if order.index(prev[j]) > order.index(word[j]):
                        return False
                    else:
                        break
                elif j == len(prev)-1 and j == len(word)-1:
                    #return True
                    continue
                #elif j == len(prev)-1:
                elif j == len(word)-1:
                    return False

            #update prev
            prev = words[i]
        return True
