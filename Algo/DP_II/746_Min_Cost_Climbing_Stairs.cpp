class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        cur = 0
        for i in range(2, len(cost) + 1):
            cur, prev = min(cost[i - 2] + prev, cost[i - 1] + cur), cur
        return cur
