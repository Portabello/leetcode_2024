'''
2451. Odd String Difference
Solved
Easy
Topics
Companies
Hint

You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

    For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].

All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.



Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation:
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".

Example 2:

Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].



Constraints:

    3 <= words.length <= 100
    n == words[i].length
    2 <= n <= 20
    words[i] consists of lowercase English letters.

'''
class Solution:
    def oddString(self, words: List[str]) -> str:
        seenonce = []
        s1 = []
        seenmore = []
        s2 = []
        for word in words:
            t = []
            for i in range(0,len(word)-1):
                #print(word[i+1],"-",word[i])
                t.append( (ord(word[i+1])-97) - (ord(word[i])-97) )
            #print(t)
            if t not in seenonce and t not in seenmore:
                seenonce.append(t)
                s1.append(word)
            elif t in seenonce:
                index = seenonce.index(t)
                seenonce.remove(t)
                del s1[index]
                seenmore.append(t)
                s2.append(word)
        #print(seenonce, s1)
        #print(seenmore, s2)
        return s1[0]
