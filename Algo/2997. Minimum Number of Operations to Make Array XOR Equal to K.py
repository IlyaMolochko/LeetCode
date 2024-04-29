class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for num in nums:
            res ^= num
        
        cnt = 0
        while k or res:
            if (k % 2) != (res % 2):
                cnt += 1
            k //= 2
            res //= 2
        return cnt
        
