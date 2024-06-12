class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0]
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        i = 0
        j = 0
        while i < len(nums):
            while cnt[j] > 0:
                nums[i] = j
                i += 1
                cnt[j] -= 1
            j += 1
