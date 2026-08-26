class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = {}
        for i in s:
            if i in sCounts:
                sCounts[i] += 1
            else:
                sCounts[i] = 1

        tCounts = {}
        for i in t:
            if i in tCounts:
                tCounts[i] += 1
            else:
                tCounts[i] = 1
        
        for i in sCounts.keys():
            if i not in tCounts:
                return False
            if sCounts[i] != tCounts[i]:
                return False
            tCounts.pop(i)

        if tCounts != {}:
            return False

        return True

