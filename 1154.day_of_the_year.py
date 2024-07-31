'''
1154. Day of the Year
Attempted
Easy
Topics
Companies
Hint
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41


Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        #print(date)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #leap = False
        if int(date[0])%4==0 and date[0]!='1900':
            #leap = True
            days_in_month[1]+=1
        #print(sum(days_in_month[0:int(date[1])-1]))
        return sum(days_in_month[0:int(date[1])-1]) + int(date[2])
        
