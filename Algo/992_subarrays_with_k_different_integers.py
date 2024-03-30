class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        dct = defaultdict(int)
        answ = 0
        cnt = 0
        while r < len(nums):
            dct[nums[r]] += 1
            if dct[nums[r]] == 1:
                k -= 1
            if k < 0:
                dct[nums[l]] -= 1
                if dct[nums[l]] == 0:
                    k += 1
                l += 1
                cnt = 0
            if k == 0:
                while dct[nums[l]] > 1:
                    dct[nums[l]] -= 1
                    l += 1
                    cnt += 1
                answ += cnt + 1
            r += 1
        return answ
