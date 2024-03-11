class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequency = Counter(s)
        answ = []
        for c in order:
            while frequency[c] > 0:
                answ.append(c)
                frequency[c] -= 1
        
        for c, f in frequency.items():
            while f > 0:
                answ.append(c)
                f -= 1  
        return ''.join(answ)
      
