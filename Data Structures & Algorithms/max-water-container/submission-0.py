class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxwater = 0
        while left < right:
            size = min(heights[left],heights[right])*(right-left)
            if size > maxwater:
                maxwater = size
                # print(f"maxwater: {maxwater}, from {heights[left]}(index {left}), {heights[right]}(index {right})")
            if heights[left] > heights[right]:
                right = right-1
            else:
                left = left+1
        return maxwater