class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        d = {}
        for c in s1:
            d[c] = d.get(c, 0) + 1

        for r in range(len(s2)):
            print(d, l, r)           
            if not s2[r] in d:
                while l <= r:
                    if s2[l] in d:
                        d[s2[l]] += 1
                    l += 1

            elif d[s2[r]] == 0:
                while s2[l] != s2[r]:
                    d[s2[l]] += 1
                    l += 1
                l += 1
            else:
                d[s2[r]] -= 1

            if r - l + 1 == len(s1):
                return True

        return False