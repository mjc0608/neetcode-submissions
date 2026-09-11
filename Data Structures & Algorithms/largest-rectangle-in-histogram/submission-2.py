import math

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        max_area = heights[0]
        for i in range(1, len(heights)):
            h = heights[i]
            while len(stack) > 0 and heights[stack[-1]] > h:
                prev = stack.pop()
                prev2 = stack[-1] if len(stack) > 0 else -1
                max_area = max(max_area, heights[prev] * (i - prev2 - 1))
            stack.append(i)
        
        # print(stack)

        i = len(heights)
        while len(stack) > 0:
            prev = stack.pop()
            prev2 = stack[-1] if len(stack) > 0 else -1
            # print(heights[prev], i - prev)
            max_area = max(max_area, heights[prev] * (i - prev2 - 1))

        return max_area