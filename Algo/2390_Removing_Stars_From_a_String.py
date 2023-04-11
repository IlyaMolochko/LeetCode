class Solution:
    def removeStars(self, s: str) -> str:
        answ = []
        for c in s:
            if c == '*':
                answ.pop()
            else:
                answ.append(c)
        return ''.join(answ)

