class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            x = (l + r) // 2
            dif = nums[x] - nums[0] + 1
            dist = x + 1
            if dif - dist >= k:
                r = x
            else:
                l = x
        return nums[l] + k - (nums[l] - nums[0] - l)
