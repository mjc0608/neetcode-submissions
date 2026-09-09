class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        for c in t:
            if c in m:
                m[c] -= 1
            else:
                return False
        
        for c in m:
            if m[c] != 0:
                return False

        return True