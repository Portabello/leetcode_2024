/*
9. Palindrome Number
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given an integer x, return true if x is a

, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
*/
#include <string.h>
#include <stdio.h>
void reverse_string(char* s){
    int i=0;
    int j=strlen(s)-1;
    char temp;

    while (i<j){
        temp = s[i];
        s[i]=s[j];
        s[j]=temp;
        i++;
        j--;
    }
}
bool isPalindrome(int x) {
    char str[20];
    snprintf(str, sizeof(str), "%d", x);
    char rev_str[20];
    strcpy(rev_str, str);
    reverse_string(rev_str);
    printf("original string %s reversed string %s", str, rev_str);
    if (strcmp(str, rev_str) == 0){
        return 1;
    }
    return 0;
}
