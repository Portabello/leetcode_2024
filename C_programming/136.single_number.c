/*
136. Single Number
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1



Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

*/
int comp(const void *a, const void *b) {
    int *n1 = (int *)a;
    int *n2 = (int *)b;

    if (*n1 > *n2) return 1;
    else if (*n1 == *n2) return 0;
    return -1;
}
int singleNumber(int* nums, int numsSize) {
    if (numsSize == 1) return nums[0];
    qsort(nums, numsSize, sizeof(nums[0]), comp);
    for (int i = 0; i < numsSize; i++) {
        if (i == (numsSize - 1)) return nums[i];
        if (nums[i] != nums[i+1]) return nums[i];
        i++;
    }
    return 0;
}
