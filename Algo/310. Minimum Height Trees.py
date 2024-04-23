class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        deg = [0] * n
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
            deg[e[0]] += 1
            deg[e[1]] += 1
        
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                deg[i] = 0
                q.append(i)
        answ = []
        while q:
            size = len(q)
            answ = []
            for _ in range(size):
                u = q.popleft()
                answ.append(u)
                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 1:
                        q.append(v)
        return answ
