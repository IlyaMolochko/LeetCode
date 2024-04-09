class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answ = 0
        for i in range(len(tickets)):
            if i <= k:
                answ += min(tickets[i], tickets[k])
            else:
                answ += min(tickets[k] - 1, tickets[i])
        return answ
