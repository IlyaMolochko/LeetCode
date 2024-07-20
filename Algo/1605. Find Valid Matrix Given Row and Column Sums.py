class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        answ = [[0] * m for _ in range(n)]
        i = 0
        j = 0
        while i < n and j < m:
            answ[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= answ[i][j]
            colSum[j] -= answ[i][j]
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return answ
