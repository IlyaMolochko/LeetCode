class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt1 = 0
        cnt2 = 0
        for s in students:
            if s == 0:
                cnt1 += 1
            else:
                cnt2 += 1
        for s in sandwiches:
            if s == 0 and cnt1 == 0:
                return cnt2
            if s == 1 and cnt2 == 0:
                return cnt1
            if s == 0:
                cnt1 -= 1
            else:
                cnt2 -= 1
        return 0
