class Solution:
    def pivotInteger(self, n: int) -> int:
        x = int(((n**2 + n) // 2)**0.5)
        if (1 + x) * x == (x + n) * (n - x + 1):
            return x
        else:
            return -1
