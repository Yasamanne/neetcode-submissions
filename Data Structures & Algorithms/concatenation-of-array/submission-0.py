class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        len_n = len(nums)
        n = 2 * len_n
        ans = []
         
        for i in range(n):
            ans.append(nums[i%len_n])
        return ans

        