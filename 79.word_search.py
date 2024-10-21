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
        ans = [0]
        #visited = []
        #given starting position of target word, recursively see if full word can be found
        def wordSearch(i, j, k, visited):
            #look up,down,left,right of [i,j]
            #print(i,j,k,ans, visited)
            new_visited = visited[:]
            new_visited.append([i,j])
            if k == len(word):
                ans[0]+=1
                return
            if i != 0:
                #up
                if board[i-1][j] == word[k]:
                    if [i-1,j] not in new_visited:
                        wordSearch(i-1,j, k+1, new_visited)
            if i != len(board)-1:
                #down
                if board[i+1][j] == word[k]:
                    if [i+1,j] not in new_visited:
                        wordSearch(i+1,j, k+1, new_visited)
            if j != 0:
                #left
                if board[i][j-1] == word[k]:
                    if [i,j-1] not in new_visited:
                        wordSearch(i,j-1, k+1, new_visited)
            if j != len(board[0])-1:
                #right
                if board[i][j+1] == word[k]:
                    if [i,j+1] not in new_visited:
                        wordSearch(i,j+1, k+1, new_visited)

        #find all occurances of the first letter of target in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    #send to helper function wordSearch
                    #visited.append([i,j])
                    #print('newsearch')
                    wordSearch(i,j,1, [])
                    #visited = []
        #print(visited)
        if ans[0]>0:
            return True
        return False
