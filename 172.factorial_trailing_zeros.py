'''
172. Factorial Trailing Zeroes
Solved
Medium
Topics
Companies

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0



Constraints:

    0 <= n <= 104



Follow up: Could you write a solution that works in logarithmic time complexity?
'''
class Solution:
    sys.set_int_max_str_digits(99999)
    def trailingZeroes(self, n: int) -> int:
        fac = 1
        for i in range(1,n+1):
            fac *= i
        def countTrailingZeros(num):
            num = str(num)[::-1]
            for i,x in enumerate(num):
                if x!='0':
                    return i
        return countTrailingZeros(fac)
