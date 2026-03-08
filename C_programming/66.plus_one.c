/*
66. Plus One
Solved
Easy
Topics
premium lock iconCompanies

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].



Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.

*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    //prescan if digits are all 9's we need an extra int in the array
    int nine_found = 1;
    for (int i = 0; i<digitsSize; i++){
        if (digits[i] != 9){
            nine_found = 0;
            break;
        }
    }

    int *ans = malloc((digitsSize+nine_found) * sizeof(int));
    int carry = 0;
    for (int i=digitsSize-1; i>=0; i--){
        //printf("%d\n",digits[i]);
        //add one
        if (i == digitsSize-1){
            if ((digits[i] + 1) > 9){
                carry = 1;
                ans[i + nine_found] = 0;
            }
            else{
                ans[i + nine_found] = digits[i] + 1;
            }
        }
        else{
            if ((digits[i] + carry) > 9){
                carry = 1;
                ans[i + nine_found] = 0;
            }
            else{
                ans[i + nine_found] = digits[i] + carry;
                carry = 0;
            }
        }
    }
    if(nine_found == 1){
        ans[0] = 1;
    }
    //for (int i = 0; i<(digitsSize+nine_found); i++){
    //    printf("ans[%d] : %d\n", i, ans[i]);
    //}
    *returnSize = digitsSize + nine_found;
    return ans;
}
