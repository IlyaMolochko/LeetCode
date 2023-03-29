class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        answ = 0
        s = 0
        i = len(satisfaction) - 1
        while i >= 0 and s + satisfaction[i] > 0:
            s += satisfaction[i]
            answ += s
            i -= 1
        return answ
