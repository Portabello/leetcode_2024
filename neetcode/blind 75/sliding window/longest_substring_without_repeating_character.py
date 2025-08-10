class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0,0
        longest_substring = 0
        substring_set = set(s[0])
        while True:
            longest_substring = max(longest_substring, r-l+1)
            if r==len(s)-1:
                break
            if s[r+1] in substring_set:
                while l<=r:
                    substring_set.remove(s[l])
                    l+=1
                    if s[r+1] not in substring_set:
                        break
            else:
                substring_set.add(s[r+1])
                r+=1
        return longest_substring
            #end case
