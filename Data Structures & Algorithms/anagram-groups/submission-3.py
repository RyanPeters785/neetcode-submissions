class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s in anagrams:
                anagrams[s].append(word)
            else:
                anagrams[s] = [word]
        
        output = []
        for a in anagrams.keys():
            output.append(anagrams[a])

        return output

