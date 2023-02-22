class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) - 1
        r = sum(weights) + 1
        while r - l > 1:
            x = (l + r) // 2
            cnt = 1
            s = 0
            for i in range(len(weights)):
                if s + weights[i] <= x:
                    s += weights[i]
                else:
                    cnt += 1
                    s = weights[i]
            if cnt <= days:
                r = x
            else:
                l = x
        return r
