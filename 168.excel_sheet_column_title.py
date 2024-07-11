tans = ""
class Solution:
    ansx = ""
    def convertToTitle(self, columnNumber: int) -> str:
        global tans
        tans = ""
        self.recurs(columnNumber)
        return tans
    def recurs(self, x):
        global tans
        mapp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        t = mapp[int(x%26)-1]
        if(x%26 == 0):
            tans = 'A' + tans
        else:
            tans = t + tans
        print(t, 'next', int(x/26))
        if x <= 26:
            return 0
        else:
            self.recurs(int(x/26))
