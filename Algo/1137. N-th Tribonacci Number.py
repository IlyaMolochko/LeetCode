class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        fourth = 2
        if n == 0:
            return 0
        elif n < 3:
            return 1
        for i in range(3, n + 1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
        return fourth
