'''
2032. Two Out of Three
Solved
Easy
Topics
Companies
Hint
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.



Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.



Constraints:

    1 <= nums1.length, nums2.length, nums3.length <= 100
    1 <= nums1[i], nums2[j], nums3[k] <= 100


'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = set()
        #compare 1 and 2
        t12 = set(nums1).intersection(set(nums2))
        #print(t12)
        #compare 2 and 3
        t23 = set(nums2).intersection(set(nums3))
        #print(t23)
        #compare 1 and 3
        t13 = set(nums1).intersection(set(nums3))
        #print(t13)
        t12.update(t23)
        t12.update(t13)
        return t12
