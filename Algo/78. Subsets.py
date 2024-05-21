class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        msk = (1 << len(nums))
        answ = []
        for i in range(msk):
            answ.append([])
            for j in range(len(nums)):
                if i & (1 << j):
                    answ[-1].append(nums[j])
        return answ
