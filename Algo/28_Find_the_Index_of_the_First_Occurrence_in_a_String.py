class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack
        n = len(s)
        z = [0] * n
        l = 0
        r = 0
        for i in range(1, n):
            if r >= i:
                z[i] = min(z[i - l], r - i + 1)
            while z[i] + i < n and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if z[i] > r:
                l = i
                r = z[i] + i - 1
            if z[i] == len(needle):
                return i - z[i] - 1
        return -1
