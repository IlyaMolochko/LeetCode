class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        answ = 0
        for i in range(2, n + 1):
            answ = (answ + k) % i
        return answ + 1
