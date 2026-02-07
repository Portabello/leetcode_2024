/*
125. Valid Palindrome
Solved
Easy
Topics
premium lock iconCompanies

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

*/
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_valid_chars(char *s) {
    int count = 0;
    int index = 0;
    while (s[index] != '\0') {
        if (isalpha(s[index]) || isdigit(s[index])) {
            count++;
        }
        index++;
    }
    return count;
}
char *clean_string(char *s, char *clean_s) {
    int s_index = 0, clean_s_index = 0;
    while (s[s_index] != '\0') {
        if (isalpha(s[s_index]) || isdigit(s[s_index])) {
            clean_s[clean_s_index++] = tolower(s[s_index++]);
        }
        else {
            s_index++;
        }
    }
    clean_s[clean_s_index] = '\0';
    return clean_s;
}
char *reverse_string(char *s, char *s_reverse, int size) {
    int index = 0;
    for (int i = size - 1; i >= 0; i--) {
        s_reverse[index++] = s[i];
    }
    s_reverse[index] = '\0';
    return s_reverse;
}
bool isPalindrome(char* s) {
    int count = count_valid_chars(s);
    //printf("count_valid_chars: %d\n", count);
    char *s_clean = malloc((count + 1) * sizeof(char));
    s_clean = clean_string(s, s_clean);
    //printf("cleaned string %s\n", clean_s);
    char *s_reverse = malloc((count + 1) * sizeof(char));
    s_reverse = reverse_string(s_clean, s_reverse, count);
    //printf("reversed string %s\n", s_reverse);
    if (strcmp(s_reverse, s_clean) == 0) {
        return true;
    }
    return false;
}
