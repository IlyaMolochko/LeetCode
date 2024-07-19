class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        mn = [float('inf')] * n
        mx = [0] * m
        for i in range(n):
            for j in range(m):
                mn[i] = min(mn[i], matrix[i][j])
                mx[j] = max(mx[j], matrix[i][j])
        answ = []
        for i in range(n):
            for j in range(m):
                if mn[i] == mx[j]:
                    answ.append(matrix[i][j])
        return answ
