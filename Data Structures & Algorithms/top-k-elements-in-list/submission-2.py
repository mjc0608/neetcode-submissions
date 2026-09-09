import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        m = {}

        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        for num in m:
            heapq.heappush_max(h, (m[num], num))
        
        r = []
        for i in range(0, k):
            r.append(heapq.heappop_max(h)[1])

        return r