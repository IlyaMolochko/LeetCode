class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        cnt = 1
        l = points[0][1]
        for i in range(len(points)):
            if l < points[i][0]:
                l = points[i][1]
                cnt += 1
        return cnt
