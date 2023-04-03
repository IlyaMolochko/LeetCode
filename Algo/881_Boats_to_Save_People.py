class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        answ = 0
        while l <= r:
            answ += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return answ
