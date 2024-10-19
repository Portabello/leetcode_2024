'''
72. Edit Distance
Solved
Medium
Topics
Companies

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character



Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')



Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.

'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        #print(dp, len(dp))
        #complete outer edges
        for i in range(0,len(dp)):
            #print('dp[',i,'][',len(dp[0])-1,']=',len(dp)-1-i)
            dp[i][len(dp[0])-1] = len(dp)-1-i
        for j in range(len(dp[0])):
            dp[len(dp)-1][j] = len(dp[0])-1-j
        #print(dp)
        #complete bottom up
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                #print(i,j)
                #compare = 1 if word1[i]!=word2[j] else 0
                #print(word1[i],'?=',word2[j], '...', compare)
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1]) +1
        #rint(dp)
        return dp[0][0]
