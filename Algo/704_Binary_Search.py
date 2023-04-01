class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m
            else:
                return m
        return -1
