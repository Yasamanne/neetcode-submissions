class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            max_area = max(max_area, w*h)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_area

        