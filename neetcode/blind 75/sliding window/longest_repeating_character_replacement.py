class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,1
        max_substring = 0
        while r<=len(s):
            #evaluate substring
            substring = s[l:r]
            #print(substring)
            counter = Counter(substring)
            max_frequency_in_substring = 0
            for x in counter:
                max_frequency_in_substring = max(max_frequency_in_substring, counter[x])
            cur_k = len(substring) - max_frequency_in_substring

            if cur_k >k:
                l+=1
            else:
                max_substring = max(max_substring, len(substring))
                r+=1
        return max_substring
