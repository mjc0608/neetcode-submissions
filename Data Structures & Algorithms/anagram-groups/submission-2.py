class Solution:
    def sortString(self, s):
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            sortedStr = self.sortString(s)
            if sortedStr in m:
                m[sortedStr].append(s)
            else:
                m[sortedStr] = [s]
        
        r = []
        for s in m:
            r.append(m[s])
        return r