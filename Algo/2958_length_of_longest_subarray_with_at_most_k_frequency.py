class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        answ = 0
        l = 0
        r = 0
        dct = defaultdict(int)
        while r < len(nums):
            dct[nums[r]] += 1
            while dct[nums[r]] > k:
                dct[nums[l]] -= 1
                l += 1
            answ = max(answ, r - l + 1)
            r += 1
        return answ
