'''
57. Insert Interval
Solved
Medium
Topics
Companies
Hint

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105

'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge_into = []
        for x in intervals:
            if (newInterval[0] >= x[0] and newInterval[0] <= x[1]) or (newInterval[1] >= x[0] and newInterval[1] <= x[1]) or (newInterval[0] <= x[0] and newInterval[1] >= x[1]):
                #print('merge found! ', x)
                merge_into.append(x)
        for x in merge_into:
            if x in intervals:
                intervals.remove(x)
        #print(intervals)
        merge_into.append(newInterval)
        min_val, max_val = float('inf'), -1
        for x in merge_into:
            for y in x:
                min_val = min(min_val, y)
                max_val = max(max_val, y)
        inserted_interval = [min_val, max_val]
        #print(inserted_interval)
        intervals.append(inserted_interval)
        intervals.sort()
        return intervals
