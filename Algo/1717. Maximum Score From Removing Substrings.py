class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x
        
        answ = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if s[i] == 'a':
                cnt1 += 1
            elif s[i] == 'b':
                if cnt1 > 0:
                    cnt1 -= 1
                    answ += x
                else:
                    cnt2 += 1
            else:
                answ += min(cnt1, cnt2) * y
                cnt1 = 0
                cnt2 = 0
        answ += min(cnt1, cnt2) * y
        return answ
