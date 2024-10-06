'''
2660. Determine the Winner of a Bowling Game
Solved
Easy
Topics
Companies
Hint

You are given two 0-indexed integer arrays player1 and player2, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:

    2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
    Otherwise, it is xi.

The score of the player is the sum of the values of their n turns.

Return

    1 if the score of player 1 is more than the score of player 2,
    2 if the score of player 2 is more than the score of player 1, and
    0 in case of a draw.



Example 1:

Input: player1 = [5,10,3,2], player2 = [6,5,7,3]

Output: 1

Explanation:

The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.

The score of player 2 is 6 + 5 + 7 + 3 = 21.

Example 2:

Input: player1 = [3,5,7,6], player2 = [8,10,10,2]

Output: 2

Explanation:

The score of player 1 is 3 + 5 + 7 + 6 = 21.

The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.

Example 3:

Input: player1 = [2,3], player2 = [4,1]

Output: 0

Explanation:

The score of player1 is 2 + 3 = 5.

The score of player2 is 4 + 1 = 5.

Example 4:

Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]

Output: 2

Explanation:

The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.

The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.



Constraints:

    n == player1.length == player2.length
    1 <= n <= 1000
    0 <= player1[i], player2[i] <= 10

'''
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def playerScore(player):
            score = 0
            # 0 if no double points, 1 if double points used once, 2 if double points used twice
            double_points = 0
            for move in player:
                if double_points:
                    #print('++',move*2)
                    score += move*2
                    if double_points == 2:
                        double_points = 0
                    else:
                        double_points += 1
                else:
                    #print('++',move)
                    score += move
                if move==10:
                    double_points = 1

            return score
        player1score = playerScore(player1)
        #print(player1score)
        player2score = playerScore(player2)
        #print(player2score)




        if player1score ==player2score:
            return 0
        if player1score > player2score:
            return 1
        return 2
