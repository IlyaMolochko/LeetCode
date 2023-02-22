class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return first
        elif n == 1:
            return second
        for i in range(2, n + 1):
            second, first = first + second, second
        return second
