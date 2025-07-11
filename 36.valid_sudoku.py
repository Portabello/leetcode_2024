'''
36. Valid Sudoku
Solved
Medium
Topics
Companies

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.



Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.



Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_sub_box_valid(x,y,board):
            already_seen = []
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j] in already_seen and board[i][j] != ".":
                        return False
                    already_seen.append(board[i][j])
            return True
        def check_column_valid(j,board):
            already_seen = []
            for i in range(9):
                if board[i][j] in already_seen and board[i][j] != ".":
                    return False
                already_seen.append(board[i][j])
            return True
        def check_row_valid(i,board):
            already_seen = []
            for j in range(9):
                if board[i][j] in already_seen and board[i][j] != ".":
                    return False
                already_seen.append(board[i][j])
            return True
        sub_box_origins = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        #check columns
        for j in range(9):
            if check_column_valid(j, board) == False:
                #print('invalid column found at ', j)
                return False
        #check roww
        for i in range(9):
            if check_row_valid(i, board) == False:
                #print('invalid row found at ', i)
                return False
        #check sub boxes
        for box in sub_box_origins:
            if check_sub_box_valid(box[0], box[1], board) == False:
                #print('invalid subbox found at ', box)
                return False
        return True
