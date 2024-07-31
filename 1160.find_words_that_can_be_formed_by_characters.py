'''
1160. Find Words That Can Be Formed by Characters
Solved
Easy
Topics
Companies
Hint
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        ans = 0
        chars = list(chars)
        for word in words:
            clist = chars.copy()
            valid = True
            for c in word:
                if c not in clist:
                    valid = False
                else:
                    clist.remove(c)
            if valid:
                ans += len(word)
        return ans
        '''
        ans = 0
        char_hash = {}
        for c in chars:
            if c in char_hash:
                char_hash[c]+=1
            else:
                char_hash[c]=1
        #word_hash = {}
        for word in words:
            word_hash = {}
            valid = True
            for c in word:
                if c in word_hash:
                    word_hash[c]+=1
                else:
                    word_hash[c]=1
                if c in char_hash:
                    if word_hash[c] > char_hash[c]:
                        valid = False
                        break
                elif c not in char_hash:
                    valid = False
                    break
            if valid:
                ans += len(word)
        return ans
