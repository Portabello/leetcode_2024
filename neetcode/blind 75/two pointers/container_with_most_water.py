class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1

        max_container = 0
        while i<j:
            cur_container = min(heights[i], heights[j]) * (j-i)
            max_container = max(cur_container, max_container)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return max_container
