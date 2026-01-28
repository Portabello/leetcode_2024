/*
111. Minimum Depth of Binary Tree
Solved
Easy
Topics
premium lock iconCompanies

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5



Constraints:

    The number of nodes in the tree is in the range [0, 105].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int min_depth = -1;
void traverse(struct TreeNode *node, int depth){
    if (node == NULL) return;
    //printf("node: %d node_depth: %d \n", node->val, depth);
    if (node->left == NULL && node->right == NULL){
        if (depth < min_depth || min_depth == -1) {
            //printf("updating mindepth to %d\n", depth);
            min_depth = depth;
        }
        return;
    }
    traverse(node->left, depth+1);
    traverse(node->right, depth+1);
}
int minDepth(struct TreeNode* root) {
    min_depth = -1;
    if (root == NULL) return 0;
    traverse(root, 1);
    return min_depth;
}
