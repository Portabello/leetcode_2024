class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_with_freq = []
        for s in strs:
            strs_with_freq.append([s, Counter(s)])
        pairs = []
        for x in strs_with_freq:
            found = False
            for i,y in enumerate(pairs):
                if x[1] == y[0][1]:
                    pairs[i].append(x)
                    found = True
            if not found:
                pairs.append([x])
        #print(pairs)
        ans = []
        for x in pairs:
            t = []
            for y in x:
                t.append(y[0])
            ans.append(t)
        return ans
