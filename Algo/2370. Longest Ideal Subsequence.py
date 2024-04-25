class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26

        answ = 0
        for i in range(n):
            cur = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - cur) <= k:
                    best = max(best, dp[prev])
            
            dp[cur] = max(dp[cur], best + 1)
            answ = max(answ, dp[cur])
        return answ
