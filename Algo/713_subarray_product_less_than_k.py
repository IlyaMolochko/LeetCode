class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        v = 1
        l = 0
        r = 0
        answ = 0
        while r < len(nums):
            v *= nums[r]
            while l <= r and v >= k:
                v /= nums[l]
                l += 1
            answ += r - l + 1
            r += 1
        return answ
