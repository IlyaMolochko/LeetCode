class Solution:
    def partitionString(self, s: str) -> int:
        pos = [-1] * 26
        cnt = 1
        l = 0
        for i in range(len(s)):
            if pos[ord(s[i]) - ord('a')] >= l:
                cnt += 1
                l = i
            pos[ord(s[i]) - ord('a')] = i
        return cnt
