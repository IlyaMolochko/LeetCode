class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        C^2_{1 + 2 - 1} = 1, C^2_{4} = 6
        00, 11, 22, 01, 12, 02
        """
        i = 0
        answ = 0
        while i < len(nums):
            cnt = 0
            while i < len(nums) and nums[i] != 0:
                i += 1
            while i < len(nums) and nums[i] == 0:
                cnt += 1
                i += 1
            answ += (cnt + 1) * cnt // 2
        return answ
