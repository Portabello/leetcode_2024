'''
97. Interleaving String
Attempted
Medium
Topics
premium lock iconCompanies

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m

respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.



Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true



Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.



Follow up: Could you solve it using only O(s2.length) additional memory space?
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ans = [False]
        def recurse(s1, s2, s3):
            if len(s1)==0 and len(s2)==0 and len(s3)==0:
                ans[0]=True
                return
            #if len(s1)==0 and s2[0]!=s3[0]:
            #    return
            #if len(s2)==0 and s1[0]!=s3[0]:
            #    return
            #if s1[0]!=s3[0] and s2[0]!=s3[0]:
            #    return
            if len(s1)!=0 and len(s3)!=0:
                if s1[0]==s3[0]:
                    recurse(s1[1:], s2, s3[1:])
            if len(s2)!=0 and len(s3)!=0:
                if s2[0]==s3[0]:
                    recurse(s1, s2[1:], s3[1:])
        recurse(s1, s2, s3)
        return ans[0]
