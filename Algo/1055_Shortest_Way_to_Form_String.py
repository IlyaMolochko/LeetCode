class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        chars = set(source)
        for c in target:
            if c not in chars:
                return -1
        n = len(source)
        i = 0
        cnt = 0
        for c in target:
            if i == 0:
                cnt += 1
            while source[i] != c:
                i = (i + 1) % n
                if i == 0:
                    cnt += 1
            i = (i + 1) % n
        return cnt
