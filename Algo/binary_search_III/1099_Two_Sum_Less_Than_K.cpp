class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        mx = -1
        for i in range(1, len(nums)):
            l = -1
            r = i
            while r - l > 1:
                x = (l + r) // 2
                if nums[x] + nums[i] < k:
                    l = x
                else:
                    r = x
            if l != -1 and nums[l] + nums[i] > mx:
                mx = nums[l] + nums[i]
        return mx
