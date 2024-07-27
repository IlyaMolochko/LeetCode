class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        answ = 0
        dp = [[float('inf')] * 26 for _ in range(26)]
        for u, v, w in zip(original, changed, cost):
            i = ord(u) - ord('a')
            j = ord(v) - ord('a')
            dp[i][j] = min(dp[i][j], w)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        for u, v in zip(source, target):
            if u != v:
                i = ord(u) - ord('a')
                j = ord(v) - ord('a')
                if dp[i][j] == float('inf'):
                    return -1
                else:
                    answ += dp[i][j]
        return answ
