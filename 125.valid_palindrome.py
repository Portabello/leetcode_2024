"""
125. Valid Palindrome
Easy
8.6K
8.1K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = re.sub(r'\W+', '', s).lower()
        stripped_s = stripped_s.replace("_", "")
        reverse_stripped_s = stripped_s[::-1]       
        if(stripped_s == reverse_stripped_s):
            return True
        return False
