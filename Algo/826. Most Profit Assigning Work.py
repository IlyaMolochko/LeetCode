class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mx = max(worker)
        jobs = [0] * (mx + 1)
        for i in range(len(difficulty)):
            if difficulty[i] <= mx:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        
        for i in range(1, mx + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        answ = 0
        for i in worker:
            answ += jobs[i]
        return answ
