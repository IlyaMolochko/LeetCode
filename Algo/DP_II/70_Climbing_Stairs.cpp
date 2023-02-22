class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        for i in range(n):
            cur, prev = cur + prev, cur
        return cur
