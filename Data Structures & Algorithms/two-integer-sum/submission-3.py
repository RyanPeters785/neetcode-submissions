class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in indices:
                return [indices[val][0], i]

            if nums[i] in indices:
                indices[nums[i]].append(i)
            else:
                indices[nums[i]] = [i]
                    
                
                
                    
                
            