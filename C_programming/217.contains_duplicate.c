/*
217. Contains Duplicate
Solved
Easy
Topics
premium lock iconCompanies

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

*/
int comp(const void *a, const void *b) {
    int *n1 = (int *)a;
    int *n2 = (int *)b;
    if (*n1 > *n2) return 1;
    if (*n1 == *n2) return 0;
    return -1;
}
bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize == 1) return false;
    qsort(nums, numsSize, sizeof(nums[0]), comp);
    int prev = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == prev) return true;
        prev = nums[i];
    }
    return false;
}
