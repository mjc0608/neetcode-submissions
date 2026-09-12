class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existed = set()
        l = 0
        r = 0
        res = 0
        while r != len(s):
            if not s[r] in existed:
                # print(f"{existed} add r={r} val={s[r]}")

                existed.add(s[r])
                r += 1
            else:
                res = max(res, len(existed))
                while s[l] != s[r]:
                    # print(f"{existed} remove l={l} val={s[l]} r={r}")
                    existed.remove(s[l])
                    l += 1
                l += 1
                r += 1
        res = max(res, len(existed))
        return res