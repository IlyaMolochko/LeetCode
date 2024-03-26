class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        inf = 5000000000
        answ = len(nums)
        for i in range(len(nums)):
            j = nums[i]
            while j <= len(nums) and j >= 1:
                t = nums[j - 1]
                nums[j - 1] = inf
                j = t
        for i in range(len(nums)):
            if nums[i] != inf:
                return i + 1
        return answ + 1
