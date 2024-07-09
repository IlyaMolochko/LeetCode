class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        l = 0
        s = 0
        for customer in customers:
            l = max(l, customer[0]) + customer[1]
            s += l - customer[0]
        return s / len(customers)
        
