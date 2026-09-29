class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, left and right of array
        # Compute the area and store it as the max result
        # move the pointer with the lower height while pinning the other
        # keep going while l < r
        
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currentArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(currentArea, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea