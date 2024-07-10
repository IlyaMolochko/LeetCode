class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answ = 0
        for op in logs:
            if op == '../':
                answ = max(0, answ - 1)
            elif op != './':
                answ += 1
        return answ
