/*
112. Path Sum
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.



Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool traverse(struct TreeNode *node, int curSum, int targetSum) {
    if (node == NULL) return false;
    curSum = curSum + node->val;
    if (node->left == NULL && node->right == NULL){
        //printf("found leaf node at %d with sum of %d\n", node->val, curSum);
        if (curSum == targetSum) return true;
        return false;
    }
    return traverse(node->left, curSum, targetSum) || traverse(node->right, curSum, targetSum);
}
bool hasPathSum(struct TreeNode* root, int targetSum) {
    if (root == NULL) return false;
    return traverse(root, 0, targetSum);
}
