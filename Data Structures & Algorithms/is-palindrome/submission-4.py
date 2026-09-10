class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def validLetter(c):
            if c >= '0' and c <= '9':
                return True
            if c >= 'a' and c <= 'z':
                return True
            if c >= 'A' and c <= 'Z':
                return True
            return False

        while i < j:
            while not validLetter(s[i]) and i < j:
                i += 1
            while not validLetter(s[j]) and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True