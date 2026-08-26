class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = [0] * 26
        for i in s:
            counts_s[ord(i) - 97] += 1

        counts_t = [0] * 26
        for j in t:
            counts_t[ord(j) - 97] += 1


        if counts_s != counts_t:
            return False
        return True