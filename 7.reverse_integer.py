"""
7. Reverse Integer
Medium
12.2K
13.2K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1


"""
import sys
sys.set_int_max_str_digits(2147483647)
answer = ""
#change to recurse(x/10, 10, ans) and keep mod at 10 instead of incrementing mod and not changing x
class Solution:
    def recurse(self, x:int, ans: str):
        global answer
        if(x%10 == x):
            ans += str(x%10)[0]
            print(x%10," ",str(x%10)[0])
            answer = ans
        else:
            ans += str(x%10)[0]
            print(x%10," ",str(x%10)[0])
            x = int(x/10)
            self.recurse(x, ans)
    def reverse(self, x: int) -> int:
        if(x <= -2147483648 or x >= 2147483647):
            return 0
        if(x>0):
            self.recurse(x, "")
            if(int(answer) >= 2147483647 or int(answer) <= -2147483648):
                return 0
            return int(answer)
        else:
            self.recurse(abs(x), "")
            if(int(answer) >= 2147483647 or int(answer) <= -2147483648):
                return 0
            return int(answer)* -1
