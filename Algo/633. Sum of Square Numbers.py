class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        i2 = 0
        while i2 <= c:
            j = c - i2
            l = -1
            r = j + 1
            while r - l > 1:
                m = (l + r) // 2
                m2 = m * m
                if m2 > j:
                    r = m
                elif m2 < j:
                    l = m
                else:
                    return True
            i += 1
            i2 = i * i
        return False
