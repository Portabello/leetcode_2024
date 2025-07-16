'''
914. X of a Kind in a Deck of Cards
Solved
Easy
Topics
premium lock iconCompanies

You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

    Each group has exactly x cards where x > 1, and
    All the cards in one group have the same integer written on them.

Return true if such partition is possible, or false otherwise.



Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.



Constraints:

    1 <= deck.length <= 104
    0 <= deck[i] < 104

'''
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_counter = Counter(deck)
        #print(deck_counter)
        value_list = []
        for x in deck_counter.values():
            value_list.append(x)
        #print(value_list)
        lcd = 1
        for i in range(2,max(value_list)+1):
            valid = True
            for x in value_list:
                if x%i!=0:
                    valid = False
            if valid:
                return True
        return False
