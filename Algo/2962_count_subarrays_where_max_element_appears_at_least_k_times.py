class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        answ = 0
        l = 0
        r = 0
        cnt = 0
        while r < len(nums):
            if nums[r] == mx:
                cnt += 1
            while cnt == k:
                if nums[l] == mx:
                    cnt -= 1
                l += 1
            answ += l
            r += 1
        return answ
