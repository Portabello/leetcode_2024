'''
49. Group Anagrams
Medium
Topics
Companies

Given an array of strings strs, group the
anagrams
together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash_table = []
        for x in strs:
            h = {}
            for c in x:
                if c in h:
                    h[c]+=1
                else:
                    h[c]=1
            strs_hash_table.append([x,h])
        #print(strs_hash_table)
        ans = []
        for x in strs_hash_table:
            found = False
            #check if hash matches a entry in ans
            for i,y in enumerate(ans):
                if y[0][1] == x[1]:
                    ans[i].append(x)
                    found= True
                    break
            #if not create a new entry
            if found == False:
                ans.append([x])
        #print(ans)
        res = []
        for x in ans:
            t = []
            for y in x:
                t.append(y[0])
            res.append(t)
        return res
