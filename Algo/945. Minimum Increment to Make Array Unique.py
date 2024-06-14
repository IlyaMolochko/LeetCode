class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        mx = max(nums)
        answ = 0
        cnt = [0] * (len(nums) + mx + 1)
        for i in nums:
            cnt[i] += 1
        for i in range(len(cnt)):
            if cnt[i] > 1:
                dup = cnt[i] - 1
                cnt[i + 1] += dup
                cnt[i] = 1
                answ += dup
        return answ
