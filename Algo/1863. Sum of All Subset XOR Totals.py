class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = 1
        r = (1 << len(nums))
        s = 0
        for i in range(l, r):
            v = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    v ^= nums[j]
            s += v
        return s
