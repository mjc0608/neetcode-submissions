class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        r = 0

        for num in nums:
            if not num in m:
                if num - 1 in m and num + 1 in m:
                    m[num] = m[num-1] + m[num+1] + 1
                    m[num-m[num-1]] = m[num]
                    m[num+m[num+1]] = m[num] 
                elif num - 1 in m:
                    m[num] = m[num-1] + 1
                    m[num-m[num-1]] = m[num]
                elif num + 1 in m:
                    m[num] = m[num+1] + 1
                    m[num+m[num+1]] = m[num] 
                else:
                    m[num] = 1

                r = max(m[num], r)
                
        return r