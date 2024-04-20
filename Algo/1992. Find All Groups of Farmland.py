class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        answ = []
        for i in range(n):
            for j in range(m):
                if land[i][j]:
                    x = i
                    y = j
                    while x < n and land[x][j]:
                        y = j
                        while y < m and land[x][y]:
                            land[x][y] = 0
                            y += 1
                        x += 1
                    answ.append([i, j, x - 1, y - 1]) 
        return answ
