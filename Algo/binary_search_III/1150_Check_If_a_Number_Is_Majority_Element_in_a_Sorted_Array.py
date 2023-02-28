class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            x = (l + r) // 2
            if nums[x] >= target:
                r = x
            else:
                l = x
        return r
    
    def upper_bound(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            x = (l + r) // 2
            if nums[x] > target:
                r = x
            else:
                l = x
        return r

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        lb = self.lower_bound(nums, target)
        up = self.upper_bound(nums, target)
        return 2 * (up - lb) > len(nums)
