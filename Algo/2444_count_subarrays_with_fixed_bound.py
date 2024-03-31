class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answ = 0
        mn = -1
        mx = -1
        l = -1
        r = 0
        while r < len(nums):
            if nums[r] < minK or nums[r] > maxK:
                l = r
            if nums[r] == minK:
                mn = r
            if nums[r] == maxK:
                mx = r
            answ += max(0, min(mn, mx) - l)
            r += 1
        return answ
