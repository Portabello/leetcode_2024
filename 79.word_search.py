'''
79. Word Search
Solved
Medium
Topics
Companies

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.



Follow up: Could you use search pruning to make your solution faster with a larger board?
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=[False]
        def recurse(i,j,visited, index):
            if index==len(word)-1:
                ans[0]=True
                return
            #board[i][j]='.'
            #top
            if i!=0:
                if board[i-1][j]==word[index+1] and (i-1,j) not in visited:
                    recurse(i-1, j,visited+[(i-1,j)], index+1)
            #bottom
            if i!=len(board)-1:
                if board[i+1][j]==word[index+1] and (i+1,j) not in visited:
                    recurse(i+1, j,visited+[(i+1,j)], index+1)
            #right
            if j!=len(board[0])-1:
                if board[i][j+1]==word[index+1] and (i,j+1) not in visited:
                    recurse(i, j+1,visited+[(i,j+1)], index+1)
            #left
            if j!=0:
                if board[i][j-1]==word[index+1] and (i,j-1) not in visited:
                    recurse(i, j-1,visited+[(i,j-1)], index+1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    recurse(i,j,[(i,j)], 0)
                if ans[0]==True:
                    return True
        return False
