class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        l_max = height[l]
        r = len(height) - 1
        r_max = height[r]

        res = 0

        while l + 1 < r:
            if l_max < r_max:
                # move l
                l_next = l + 1
                while height[l_next] <= l_max and l_next < r:
                    l_next += 1
                
                l_roof = min(height[l], height[l_next])
                for i in range(l+1, l_next):
                    res += (l_roof - height[i])
                
                l = l_next
                l_max = max(l_max, height[l])
            else:
                # move r
                r_next = r - 1
                while height[r_next] <= r_max and r_next > l:
                    r_next -= 1
                
                r_roof = min(height[r], height[r_next])
                for i in range(r-1, r_next, -1):
                    res += (r_roof - height[i])

                r = r_next
                r_max = max(r_max, height[r])

        return res


                

