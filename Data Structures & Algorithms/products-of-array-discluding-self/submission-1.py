class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProds = [1] * len(nums)
        rProds = [1] * len(nums)

        for i in range(1, len(nums)):
            lProds[i] = lProds[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rProds[i] = rProds[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(lProds[i] * rProds[i])

        return result