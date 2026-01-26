/*
100. Same Tree
Solved
Easy
Topics
premium lock iconCompanies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false



Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void countNodes(struct TreeNode *n, int *count){
    if (n == NULL) {
        (*count)++;
        return;
    }
    (*count)++;
    countNodes(n->left, count);
    countNodes(n->right, count);
}
void inorder(struct TreeNode *n, int *arr, int *index){
    if (n == NULL) {
        arr[*index] = 10001;
        (*index)++;
        return;
    }
    arr[*index] = n->val;
    (*index)++;
    inorder(n->left, arr, index);
    inorder(n->right, arr, index);
}
void preorder(struct TreeNode *n, int *arr, int *index){
    if (n == NULL) {
        arr[*index] = 10001;
        (*index)++;
        return;
    }
    inorder(n->left, arr, index);
    arr[*index] = n->val;
    (*index)++;
    inorder(n->right, arr, index);
}
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    int p_len = 0;
    int q_len = 0;
    countNodes(p, &p_len);
    countNodes(q, &q_len);
    //check len is same
    if (q_len != p_len) {return false;}

    int *p_arr_inorder = malloc(sizeof(int) * p_len);
    int *p_arr_preorder = malloc(sizeof(int) * p_len);
    int index = 0;
    inorder(p, p_arr_inorder, &index);
    index = 0;
    preorder(p, p_arr_preorder, &index);
    /*
    printf("\ninorder p arr:\n");
    for (int i=0; i<p_len; i++){
        printf("%d ,", p_arr_inorder[i]);
    }
    printf("\npreorder p arr:\n");
    for (int i=0; i<p_len; i++){
        printf("%d ,", p_arr_preorder[i]);
    }
    */
    int *q_arr_inorder = malloc(sizeof(int) * q_len);
    int *q_arr_preorder = malloc(sizeof(int) * q_len);
    index = 0;
    inorder(q, q_arr_inorder, &index);
    index = 0;
    preorder(q, q_arr_preorder, &index);
    /*
    printf("\ninorder q arr:\n");
    for (int i=0; i<q_len; i++){
        printf("%d ,", q_arr_inorder[i]);
    }
    printf("\npreorder q arr:\n");
    for (int i=0; i<q_len; i++){
        printf("%d ,", q_arr_preorder[i]);
    }
    */
    for (int i=0; i<p_len; i++){
        if (q_arr_preorder[i] != p_arr_preorder[i]) {return false;}
        if (q_arr_inorder[i] != q_arr_inorder[i]) {return false;}
    }
    return true;
}
