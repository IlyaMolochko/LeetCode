class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = totalTrips * max(time) + 1
        while r - l > 1:
            x = (l + r) // 2
            f = False
            cnt = 0
            for i in range(len(time)):
                cnt += x // time[i]
            if cnt >= totalTrips:
                r = x
            else:
                l = x
        return r
