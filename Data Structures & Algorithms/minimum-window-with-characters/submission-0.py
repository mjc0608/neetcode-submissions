import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1

        l = 0
        window = {}
        have = 0
        need = len(d)
        best_idx = (0, 0)
        best_len = math.inf
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == d.get(s[r], 0):
                have += 1
            if need == have:
                while need == have:
                    if r - l + 1 < best_len:
                        best_len = r - l + 1
                        best_idx = (l, r+1)

                    if window[s[l]] == d.get(s[l], 0):
                        have -= 1
                    window[s[l]] -= 1
                    l += 1
                
        return s[best_idx[0]:best_idx[1]]

                