/*
20. Valid Parentheses
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

*/
#include <stdio.h>
#include <stdlib.h>
bool isValid(char* s) {
    char stack[10000];
    int stack_index = 0;
    for (int i=0; s[i]!='\0'; i++){
        //printf("%c\n",s[i]);
        //if closing parentheses, check and pop from stack
        if (s[i] == ')' || s[i] == '}' || s[i] == ']'){
            //EDGE CASE: string starts with closing bracket - RETURN FALSE
            if (stack_index <= 0) return 0;
            else if (s[i] == ')' && stack[stack_index-1] == '('){
                stack[stack_index-1] = '\0';
                stack_index--;
            }
            else if (s[i] == '}' && stack[stack_index-1] == '{'){
                stack[stack_index-1] = '\0';
                stack_index--;
            }
            else if (s[i] == ']' && stack[stack_index-1] == '['){
                stack[stack_index-1] = '\0';
                stack_index--;
            }
            //improper opening bracket in stack RETURN FALSE
            else return 0;
        }
        //if opening parenthesis, append to stack
        else{
            stack[stack_index] = s[i];
            stack_index++;
        }
    }
    //if stack empty - RETURN TRUE
    if (stack_index == 0) return 1;
    //if stack still has elements - RETURN FALSE
    return 0;
}
