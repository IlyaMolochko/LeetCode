class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        r = 0
        while l < len(s) and r < len(t):
            while l < len(s) and s[l] != t[r]:
                l += 1
            if l < len(s) and s[l] == t[r]:
                l += 1
                r += 1
            else:
                return len(t) - r
        return len(t) - r
