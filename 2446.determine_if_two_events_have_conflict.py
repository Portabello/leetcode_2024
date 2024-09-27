'''
2446. Determine if Two Events Have Conflict
Solved
Easy
Topics
Companies
Hint

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

    event1 = [startTime1, endTime1] and
    event2 = [startTime2, endTime2].

Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.



Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.

Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.

Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.



Constraints:

    event1.length == event2.length == 2
    event1[i].length == event2[i].length == 5
    startTime1 <= endTime1
    startTime2 <= endTime2
    All the event times follow the HH:MM format.

'''
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        a_start = self.convertTime(event1[0])
        a_end = self.convertTime(event1[1])
        b_start = self.convertTime(event2[0])
        b_end = self.convertTime(event2[1])
        return b_start <= a_start <= b_end or \
               b_start <= a_end <= b_end or \
               a_start <= b_start <= a_end or \
               a_start <= b_end <= a_end

    def convertTime(self, time):
        return int(time[:2])*60 + int(time[3:])
