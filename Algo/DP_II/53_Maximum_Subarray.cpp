class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        answ = nums[0]
        for i in range(len(nums)):
            s += nums[i]
            answ = max(answ, s)
            if s < 0:
                s = 0
        return answ
