/*
119. Pascal's Triangle II
Solved
Easy
Topics
premium lock iconCompanies

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]



Constraints:

    0 <= rowIndex <= 33



Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize) {
    int *previous_row = NULL;
    *returnSize = rowIndex + 1;
    for (int i = 0; i <= rowIndex; i++) {
        //base case
        if (previous_row == NULL) {
            previous_row = malloc(sizeof(int));
            previous_row[0] = 1;
        }
        else {
            int *new_row = malloc((i+1) *sizeof(int));
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    new_row[j] = 1;
                }
                else{
                    new_row[j] = previous_row[j-1] + previous_row[j];
                }
            }
            free(previous_row);
            previous_row = new_row;
        }
    }
    return previous_row;
}
