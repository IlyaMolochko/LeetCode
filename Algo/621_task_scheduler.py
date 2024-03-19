class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        mx = 0
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
            mx = max(mx, freq[ord(t) - ord('A')])
        total = (mx - 1) * (n + 1)
        for f in freq:
            if f == mx:
                total += 1
        
        return max(len(tasks), total)
    
