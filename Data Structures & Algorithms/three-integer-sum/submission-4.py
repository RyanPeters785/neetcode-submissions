class Solution:
    def twoSum(self, nums, k): 
        d = set() 
        result = set() 
        
        for i in nums: 
            if k - i in d: 
                result.add((k - i, i))
            d.add(i)
        
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            val = -nums[i]
            for x, y in self.twoSum(nums[i+1:], val):
                result.append([nums[i], x, y])
        return result
            
        

