class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        res = (j - i) * min(heights[i], heights[j])
        while i < j:
            if (heights[i] > heights[j]):
                # move j
                j -= 1
                res = max(res, (j - i) * min(heights[i], heights[j]))
            else:
                # move i
                i += 1
                res = max(res, (j - i) * min(heights[i], heights[j]))

        return res