class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answ = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            answ.append(intervals[i])
            i += 1
        if i == len(intervals):
            answ.append(newInterval)
            return answ
        else:
            if intervals[i][0] > newInterval[1]:
                answ.append(newInterval)
            else:
                answ.append([min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])])
                while i < len(intervals) and answ[-1][1] >= intervals[i][0]:
                    answ[-1][1] = max(answ[-1][1], intervals[i][1])
                    i += 1
            while i < len(intervals):
                answ.append(intervals[i])
                i += 1
        return answ
