import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 0
        l = 1
        for pile in piles:
            r = max(r, pile)

        best_k = r
        while l <= r:
            mid = (l + r) // 2
            actual_h = 0
            for pile in piles:
                actual_h += math.ceil(pile / mid)
            if actual_h <= h:
                # eat too slow
                best_k = min(best_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return best_k
                