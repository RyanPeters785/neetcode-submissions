class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        longestLength = 0
        
        for i in nums:
            if i - 1 not in nums:
                k = i
                while k in nums:
                    k += 1

                if k - i > longestLength:
                    longestLength = k - i

        return longestLength

