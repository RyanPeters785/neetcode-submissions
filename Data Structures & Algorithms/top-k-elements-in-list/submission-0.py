class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        a = {}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        b = {}
        for i in a.keys():
            if a[i] in b:
                b[a[i]].append(i)
            else:
                b[a[i]] = [i]
        
        keys = sorted(b.keys(), reverse = True)
        print(keys)
        
        result = []
        for i in keys:
            for j in b[i]:
                result.append(j)

        return result[:k]