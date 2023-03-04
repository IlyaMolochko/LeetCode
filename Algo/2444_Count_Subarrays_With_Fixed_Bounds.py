class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answ = 0
        mn = -1
        mx = -1
        l = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                l = i
            if nums[i] == minK:
                mn = i
            if nums[i] == maxK:
                mx = i
            answ += max(0, min(mn, mx) - l)
        
        return answ
