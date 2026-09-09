class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            s = s.replace("\\", "\\\\")
            r += "\\b"
            r += s
            r += "\\e"
        print(r)
        return r

    def decode(self, s: str) -> List[str]:
        r = []
        item = ""
        i = 0
        while i < len(s):
            if s[i] != "\\":
                item += s[i]
                i += 1
            else:
                if i + 1 < len(s):
                    if s[i+1] == "\\":
                        item += "\\"
                        i += 2
                    elif s[i+1] == "b":
                        item = ""
                        i += 2
                    elif s[i+1] == "e":
                        r.append(item)
                        i += 2

        return r
