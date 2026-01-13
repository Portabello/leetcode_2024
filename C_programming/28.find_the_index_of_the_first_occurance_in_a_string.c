/*
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
premium lock iconCompanies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

*/
int strStr(char* haystack, char* needle) {
    for (int i = 0; haystack[i] != '\0'; i++){
        //printf("%c\n",haystack[i]);
        int j = i;
        int k = 0;
        while(1){
            //printf("comparing haystack - %c - to needle - %c -\n",haystack[j],needle[k]);
            if (needle[k] == '\0') return i;
            if (haystack[j] != needle[k]) break;

            j++;
            k++;
        }
        //printf("------\n");
    }
    return -1;
}
