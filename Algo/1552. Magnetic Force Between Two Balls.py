class Solution:
    def check(self, position: List[int], m: int, x: int) -> bool:
        r = position[0] + x
        cnt = 1
        for i in range(1, len(position)):
            if position[i] >= r:
                cnt += 1
                r = position[i] + x
        return cnt >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        r = position[-1]
        while r - l > 1:
            x = (r + l) // 2
            if self.check(position, m, x):
                l = x
            else:
                r = x
        return l
