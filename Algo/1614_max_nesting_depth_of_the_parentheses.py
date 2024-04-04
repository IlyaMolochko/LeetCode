class Solution:
    def maxDepth(self, s: str) -> int:
        answ = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            answ = max(answ, cnt)
        return answ
