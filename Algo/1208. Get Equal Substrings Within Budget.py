class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        answ = 0
        l = 0
        r = 0
        while r < len(s):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            while l <= r and maxCost < 0:
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
            answ = max(r - l + 1, answ)
            r += 1
        return answ
