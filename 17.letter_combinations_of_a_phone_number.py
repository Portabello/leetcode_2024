"""
17. Letter Combinations of a Phone Number
Solved
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        code = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []
        n = len(digits)

        if n==1:
            for x in code[int(digits)]:
                ans.append(x)
        if n==2:
            for x in code[int(digits[0])]:
                for y in code[int(digits[1])]:
                    ans.append(x+y)
        if n==3:
            for x in code[int(digits[0])]:
                for y in code[int(digits[1])]:
                    for z in code[int(digits[2])]:
                        ans.append(x+y+z)
        if n==4:
            for x in code[int(digits[0])]:
                for y in code[int(digits[1])]:
                    for z in code[int(digits[2])]:
                        for v in code[int(digits[3])]:
                            ans.append(x+y+z+v)
        return ans