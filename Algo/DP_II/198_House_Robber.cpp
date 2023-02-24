class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        answ = dp[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i] if i >= 3 else 0)
            answ = max(dp[i], answ)
        return answ
