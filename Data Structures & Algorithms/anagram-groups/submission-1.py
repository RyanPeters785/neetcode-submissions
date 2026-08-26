class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_counts = {}
        for i in strs:
            strs_counts[i] = [0] * 26

        for i, s in enumerate(strs):
            for j in s:
                strs_counts[strs[i]][ord(j) - ord('a')] += 1
        
        groups = []
        for i in range(len(strs)):
            added = False
            for j in groups:
                if strs_counts[strs[i]] == strs_counts[j[0]]:
                    j.append(strs[i])
                    added = True
                    break
            if not added:
                groups.append([strs[i]])
        return groups