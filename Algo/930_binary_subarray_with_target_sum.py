class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        r = 0
        s = 0
        answ = 0
        pref_zeros = 0
        while r < len(nums):
            s += nums[r]
            while l < r and (nums[l] == 0 or s > goal):
                if nums[l] == 1:
                    pref_zeros = 0
                    s -= 1
                else:
                    pref_zeros += 1
                l += 1
            
            if s == goal:
                answ += 1 + pref_zeros
            r += 1

        return answ
