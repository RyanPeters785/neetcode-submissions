class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for j, x in enumerate(nums):
            need = target - x
            
            if need in pos:
                i = pos[need]
                return [i, j] 

            if x not in pos:
                pos[x] = j