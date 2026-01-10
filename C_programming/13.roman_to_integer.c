/*
13. Roman to Integer
Solved
Easy
Topics
premium lock iconCompanies
Hint

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].


*/
#include <stdio.h>

int romanToInt(char* s) {
    int ans = 0;
    char last = 0;
    for(int i=0; s[i]!='\0'; i++){
        printf("%c", s[i]);
        if(s[i]=='V' && last=='I')
            ans += 3;
        else if(s[i]=='X' && last=='I')
            ans += 8;
        else if(s[i]=='L' && last=='X')
            ans += 30;
        else if(s[i]=='C' && last=='X')
            ans += 80;
        else if(s[i]=='D' && last=='C')
            ans += 300;
        else if(s[i]=='M' && last=='C')
            ans += 800;
        else{
            switch(s[i]){
                case 'I':
                    ans += 1;
                    break;
                case 'V':
                    ans += 5;
                    break;
                case 'X':
                    ans += 10;
                    break;
                case 'L':
                    ans += 50;
                    break;
                case 'C':
                    ans += 100;
                    break;
                case 'D':
                    ans += 500;
                    break;
                case 'M':
                    ans += 1000;
                    break;
            }
        }
        last = s[i];
    }
    return ans;
}
