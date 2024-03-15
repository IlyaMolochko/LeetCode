class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answ = nums.copy()
        for i in range(1, len(nums)):
            answ[i] *= answ[i - 1]
        answ[len(nums) - 1] = answ[len(nums) - 2]
        v = 1
        for i in range(len(nums) - 1, 0, -1):
            answ[i] = answ[i - 1] * v
            v *= nums[i]
        answ[0] = v
        return answ
         
