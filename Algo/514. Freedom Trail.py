class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def count_steps(n, cur, nxt):
            between = abs(cur - nxt)
            around = n - between
            return min(between, around)
        
        n = len(ring)
        m = len(key)

        chars = defaultdict(list)
        for i, c in enumerate(ring):
            chars[c].append(i)
        
        q = [(0, 0, 0)]
        visited = set()
        s = 0
        while q:
            s, rid, kid = heapq.heappop(q)
            if kid == m:
                break
            if (rid, kid) not in visited:
                visited.add((rid, kid))
                for nxt in chars[key[kid]]:
                    heapq.heappush(q, (s + count_steps(n, rid, nxt), nxt, kid + 1))
            

        return s + m
