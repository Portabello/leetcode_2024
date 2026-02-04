/*
101. Symmetric Tree
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traverse(struct TreeNode *l, struct TreeNode *r, bool *symmetric){
    if ((l == NULL && r != NULL) || (l != NULL && r == NULL)) {
        *symmetric = false;
        return;
    }
    if (l == NULL && r == NULL) return;
    //printf("left: %d right: %d\n", l->val, r->val);
    if (l->val != r->val){
        *symmetric = false;
        return;
    }
    traverse(l->left, r->right, symmetric);
    traverse(l->right, r->left, symmetric);
}
bool isSymmetric(struct TreeNode* root) {
    bool symmetric = true;
    traverse(root->left, root->right, &symmetric);
    return symmetric;

}
