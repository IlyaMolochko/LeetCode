class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        it = time // (n - 1)
        rest = time % (n - 1)
        if it & 1:
            return n - rest
        else:
            return rest + 1
    
