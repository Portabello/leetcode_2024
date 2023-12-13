answer = 0
class Solution:
    def climbStairs(self, n: int) -> int:
        global answer
        answer=0
        self.step(n)
        return answer
    def step(self, n: int) -> int:
        global answer
        #end con
        if(n==0):
            answer+=1
            return
        #1 step
        if(n-1>=0):
            self.step(n-1)
        #2 step
        if(n-1>=0):
            self.step(n-2)
