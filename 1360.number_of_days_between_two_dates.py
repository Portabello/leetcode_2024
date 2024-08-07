'''
1360. Number of Days Between Two Dates
Solved
Easy
Topics
Companies
Hint
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        x1=self.fdate(date1)
        x2=self.fdate(date2)
        #print(x1,x2)
        return abs(x2-x1)

    def fdate(self, date):
        date = date.split("-")
        #print(date)
        isleap=False
        if int(date[0])%4==0 and int(date[0])!=1900:
            if int(date[0])%100==0:
                if int(date[0])%400==0:
                    isleap=True
                else:
                    isleap=False
            else:
                isleap=True
        else:
            isleap=False
        #1900-year
        ans = 0
        #leap=0
        for x in range(1900,int(date[0])):
            if x%4==0 and x!=1900:
                if x%100==0:
                    if x%400==0:
                        #print('leap',x)
                        #leap+=1
                        ans+=366
                    else:
                        ans+=365
                else:
                    #print('leap',x)
                    #leap+=1
                    ans+=366
            else:
                ans+=365
        #print(date, ans, leap)
        #month
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        for x in range(0,int(date[1])-1):
            #print(x)
            if x==1 and int(date[0])%4==0 and isleap:
                ans+=29
            else:
                ans+=months[x]
        ans+=int(date[2])
        return ans
