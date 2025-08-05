'''
2396. Strictly Palindromic Number
Solved
Medium
Topics
Companies
Hint

An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.



Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.

Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.



Constraints:

    4 <= n <= 105

'''
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def dec_to_base(base, x):
            ans = ""
            if x == 0:
                return "0"
            while x>0:
                ans = str(x%base) + ans
                x = x//base
            return ans
        
        def is_palindromic(x):
            if x == x[::-1]:
                return True
            return False

        for base in range(2,n-1):
            #print('n in base ', base, ' is ', dec_to_base(base, n))
            if not is_palindromic(dec_to_base(base, n)):
                return False
        return True
