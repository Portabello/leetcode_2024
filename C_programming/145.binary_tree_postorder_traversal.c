/*
145. Binary Tree Postorder Traversal
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
 */
 #include <stdlib.h>
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
void tree_size(struct TreeNode *node, int *size){
    if (node == NULL) return;
    (*size)++;
    tree_size(node->left, size);
    tree_size(node->right, size);
}
void traverse(struct TreeNode *node, int *arr, int *index) {
    if (node == NULL) return;
    traverse(node->left, arr, index);
    traverse(node->right, arr, index);
    arr[(*index)++] = node->val;

}
int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    int size = 0;
    tree_size(root, &size);
    *returnSize = size;
    //printf("tree size %d\n", size);
    int *arr = malloc(size * sizeof(int));
    int index = 0;
    traverse(root, arr, &index);
    //for (int i =0; i<size; i++) {
    //    printf("%d:[%d]  ", i, arr[i]);
    //}
    return arr;
}
