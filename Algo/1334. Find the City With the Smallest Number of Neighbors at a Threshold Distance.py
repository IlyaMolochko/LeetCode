class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float('inf')
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        answ = -1
        fewest_reachable_count = n

        for i in range(n):
            reachable_count = sum(1 for j in range(n) if i != j and dp[i][j] <= distanceThreshold)
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                answ = i
        return answ
