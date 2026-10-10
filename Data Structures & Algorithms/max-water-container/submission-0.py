class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Score each combination by height * distance to middle

        left, right = 0, len(heights)-1
        area = 0 

        while left < right:
            new_area = min(heights[left], heights[right]) * (right - left)
            area = max(area, new_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        
        return area
