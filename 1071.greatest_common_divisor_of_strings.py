"""
1071. Greatest Common Divisor of Strings
Solved
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        hs1, hs2 = Counter(str1), Counter(str2)
        #for x in hs1:
        #    if max(hs1[x], hs2[x]) % min(hs1[x], hs2[x]) != 0:
        #        return False
        substring = str1[0]
        substring_len = 1
        valid_solution = ""
        while len(substring) <= min(len(str1), len(str2)):
            #print(substring)
            if substring * (len(str1)//len(substring)) == str1 and substring * (len(str2)//len(substring)) == str2:
                #print('valid solution found ', substring)
                valid_solution = substring
            if len(substring) == min(len(str1), len(str2)):
                break
            substring_len += 1
            substring = str1[0:substring_len]
        return valid_solution
