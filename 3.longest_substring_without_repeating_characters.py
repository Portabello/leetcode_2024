class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        maxss = None
        #change to check longest substrings first, then 1 less, then 1 less...
        #first one u find is answer

        for i,c in enumerate(s):
            for j in range (i,len(s)+1):
                #print(s[i:j])
                if len(s[i:j]) > maxlen:
                    if self.checkForDuplicateCharacters(s[i:j]):
                        maxss = s[i:j]
                        maxlen = len(s[i:j])
        return maxlen
    def checkForDuplicateCharacters(self, s):
        found = []
        for c in s:
            if c in found:
                return False
            else:
                found.append(c)
        return True
