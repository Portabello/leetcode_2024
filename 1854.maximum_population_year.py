'''
1854. Maximum Population Year
Solved
Easy
Topics
Companies
Hint
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.



Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.


Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
'''
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = {}
        for log in logs:
            for i in range(log[0],log[1]):
                if i in population:
                    population[i]+=1
                else:
                    population[i]=1
        max_i = 0
        max_year = 0
        #print(population)
        for x in population:
            if population[x]>max_i:
                #print('update',x, max_i, population[x])
                max_i=population[x]
                max_year = x
            if population[x]==max_i and x<max_year:
                max_year = x
        return max_year
