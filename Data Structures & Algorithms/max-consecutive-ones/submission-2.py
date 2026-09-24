class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        start = end = 0
        while end < len(nums):
            while start < len(nums) and nums[start] == 0:
                start += 1
            end = start
            while end < len(nums) and nums[end] == 1:
                end += 1
            
            max_ones = max(max_ones, end - start)
            if end < len(nums):
                start = end
        return max_ones
