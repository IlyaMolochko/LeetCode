class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for c in s:
            cnt += (c == '1')
        answ = ['0'] * len(s)
        answ[-1] = '1'
        cnt -= 1
        i = 0
        while cnt > 0:
            answ[i] = '1'
            cnt -= 1
            i += 1
        return ''.join(answ)
