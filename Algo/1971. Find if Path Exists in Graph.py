class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for g in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        if source == destination:
            return True
        q = deque()
        q.append(source)
        visited = [0] * n
        visited[source] = 1
        while q:
            top = q.popleft()
            if top == destination:
                return True
            for i in range(len(g[top])):
                if visited[g[top][i]] == 0:
                    q.append(g[top][i])
                    visited[g[top][i]] = 1
        return False
