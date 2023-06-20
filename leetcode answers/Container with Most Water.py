class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        INPUT: integer array of heights
        OUTPUT: maximum amount of water that the container can store
        NOTES:
        
        amount of water stored = distance * min(height)
        
        left, right at either end
        '''
        left, right = 0, len(height) - 1
        max_water = min(height[left], height[right]) * (right - left)
        while (left < right):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
        return max_water