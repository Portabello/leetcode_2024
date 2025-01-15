'''
1370. Increasing Decreasing String
Easy
Topics
Companies
Hint

You are given a string s. Reorder the string using the following algorithm:

    Remove the smallest character from s and append it to the result.
    Remove the smallest character from s that is greater than the last appended character, and append it to the result.
    Repeat step 2 until no more characters can be removed.
    Remove the largest character from s and append it to the result.
    Remove the largest character from s that is smaller than the last appended character, and append it to the result.
    Repeat step 5 until no more characters can be removed.
    Repeat steps 1 through 6 until all characters from s have been removed.

If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

Return the resulting string after reordering s using this algorithm.



Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.



Constraints:

    1 <= s.length <= 500
    s consists of only lowercase English letters.

'''
class Solution:
    def sortString(self, s: str) -> str:
        ans = ""
        s = list(s)
        while len(s)>0:
            #step 1
            smallest = None
            index = None
            for i,c in enumerate(s):
                if smallest == None:
                    smallest = c
                    index = i
                else:
                    if c < smallest:
                        smallest = c
                        index = i
            ans = ans + smallest
            s.pop(index)
            #step 2
            last = smallest
            smallest = None
            index = None
            found = False
            while True:
                for i,c in enumerate(s):
                    if c > last and smallest == None:
                        smallest = c
                        index = i
                        found = True
                    elif smallest != None:
                        if c > last and c < smallest:
                            smallest = c
                            index = i
                            found = True
                if found == False:
                    break
                ans = ans + smallest
                s.pop(index)
                last = smallest
                smallest = None
                index = None
                found = False

            print(ans)
