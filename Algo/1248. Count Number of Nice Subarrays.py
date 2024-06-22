class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answ = 0
        l = 0
        size = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] & 1:
                size += 1
            if size == k:
                cnt = 0
                while size == k:
                    size -= (nums[l] & 1)
                    cnt += 1
                    l += 1
            answ += cnt
        return answ
