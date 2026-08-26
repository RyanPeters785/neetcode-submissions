class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = -1
        for a in range(len(nums)):
            if i != -1:
                if target - nums[i] == nums[a]:
                    return [i, a]
            elif (target - nums[a]) in nums[a + 1:]:
                    i = a