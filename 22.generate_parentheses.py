'''
22. Generate Parentheses
Solved
Medium
Topics
premium lock iconCompanies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]



Constraints:

    1 <= n <= 8

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rc(cur, opencount, closedcount):
            if opencount == closedcount and opencount+closedcount == n*2:
                ans.append(cur)
                return
            if opencount < n:
                rc(cur+"(", opencount+1, closedcount)
            if closedcount < opencount:
                rc(cur+")", opencount, closedcount+1)
        rc("",0,0)
        #print(ans)
        return ans
