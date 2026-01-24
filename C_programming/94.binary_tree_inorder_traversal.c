/*
94. Binary Tree Inorder Traversal
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void traverse(struct TreeNode *node, int *ans, int *index){
    if (node == NULL) return;
    traverse(node->left, ans, index);
    ans[*index] = node->val;
    (*index)++;
    traverse(node->right, ans, index);
}

void nodeCount(struct TreeNode *root, int *count){
    if (root == NULL) return;
    nodeCount(root->left, count);
    nodeCount(root->right, count);
    (*count)++;
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int node_count = 0;
    nodeCount(root, &node_count);
    *returnSize = node_count;
    int *ans = malloc(sizeof(int) * node_count);
    int index = 0;
    traverse(root, ans, &index);
    return ans;
}
