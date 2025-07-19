class Solution:
    def maxArea(self, height: List[int]) -> int:
        # move the pointer in the lower line
        i = 1
        j = len(height)
        result = 0

        while i < j:
            h = min(height[i-1], height[j-1])
            w = j - i
            result = max(result, h * w)

            if height[j-1] <= height[i-1]:
                j-=1
            else:
                i+=1

        return result
        