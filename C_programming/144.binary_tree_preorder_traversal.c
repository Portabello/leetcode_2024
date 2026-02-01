/*
144. Binary Tree Preorder Traversal
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

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
    arr[(*index)++] = node->val;
    traverse(node->left, arr, index);
    traverse(node->right, arr, index);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
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
