/*
169. Majority Element
Solved
Easy
Topics
premium lock iconCompanies

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.


Follow-up: Could you solve the problem in linear time and in O(1) space?
*/
int comp(const void *a, const void *b) {
    int *n1 = (int *)a;
    int *n2 = (int *)b;
    if (*n1 > *n2) return 1;
    else if (*n1 == *n2) return 0;
    return -1;
}
int majorityElement(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), comp);

    int majority_element = 0;
    int majority_occurances = 0;
    int last = 0;
    int occurances = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == last) occurances++;
        else{
            if (occurances > majority_occurances) {
                majority_element = last;
                majority_occurances = occurances;
            }
            last = nums[i];
            occurances = 1;
        }
    }
    if (occurances > majority_occurances) return last;
    return majority_element;
}
