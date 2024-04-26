class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[10e20] * n for _ in range(n)]
        for j in range(n):
            dp[n - 1][j] = grid[n - 1][j]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                nxt = 10e20
                for k in range(n):
                    if k != j:
                        nxt = min(nxt, dp[i + 1][k])
                dp[i][j] = grid[i][j] + nxt
        answ = 10e20

        for j in range(n):
            answ = min(answ, dp[0][j])
        return answ
