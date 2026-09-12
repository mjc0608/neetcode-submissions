class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0

        curr_map = {}
        maxf = 0

        for r in range(len(s)):
            curr_map[s[r]] = curr_map.get(s[r], 0) + 1
            maxf = max(maxf, curr_map[s[r]])
            # print(curr_map, maxf)
            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                while r - l + 1 - maxf > k:
                    curr_map[s[l]] -= 1
                    l += 1
        
        return res
