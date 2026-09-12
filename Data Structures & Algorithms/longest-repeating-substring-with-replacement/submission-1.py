class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0

        curr_map = {}

        def curr_map_has_slot():
            if len(curr_map) == 0:
                return True
            for key in curr_map:
                if r - l - curr_map[key] < k:
                    return True
            return False
        
        while r < len(s):
            if curr_map_has_slot() or (
                s[r] in curr_map and r - l - curr_map[s[r]] <= k
            ):
                if s[r] in curr_map:
                    curr_map[s[r]] += 1
                else:
                    curr_map[s[r]] = 1
                r += 1
                res = max(res, r - l)
            else:
                # no slot available, need to pop
                if curr_map[s[l]] > 1:
                    curr_map[s[l]] -= 1
                else:
                    curr_map.pop(s[l])
                l += 1
        
        return res
