'''
654. Maximum Binary Tree
Solved
Medium
Topics
Companies

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

    Create a root node whose value is the maximum value in nums.
    Recursively build the left subtree on the subarray prefix to the left of the maximum value.
    Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.



Example 1:

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:

Input: nums = [3,2,1]
Output: [3,null,2,null,1]



Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
    All integers in nums are unique.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        res = []
        head = [None]
        def rc(arr, node, side):
            if len(arr) == 0:
                #res.append(None)
                return
            else:
                max_val = max(arr)
                max_val_index = arr.index(max_val)
                left_arr = arr[:max_val_index]
                right_arr = arr[max_val_index+1:]
                if head[0] == None:
                    head[0] = TreeNode(max_val)
                    rc(left_arr, head[0], 'left')
                    rc(right_arr, head[0], 'right')
                else:
                    if side == 'left':
                        node.left = TreeNode(max_val)
                        rc(left_arr, node.left, 'left')
                        rc(right_arr, node.left, 'right')
                    elif side == 'right':
                        node.right = TreeNode(max_val)
                        rc(left_arr, node.right, 'left')
                        rc(right_arr, node.right, 'right')

                #res.append(max_val)
                #rc(left_arr)
                #rc(right_arr)
        rc(nums, None, None)
        print(head[0])
        return head[0]