class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answ = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            answ = max(answ, math.ceil(s / (i + 1)))
        return answ
