class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def least_absolute_value_index(nums: List[int]) -> int:
            l = -1
            r = len(nums)
            while r - l > 1:
                m = (l + r) // 2
                if nums[m] >= 0:
                    r = m
                else:
                    l = m
            if r == len(nums):
                return r - 1
            elif r == 0:
                return 0
            else:
                return r - 1 if abs(nums[r - 1]) < abs(nums[r]) else r
        
        i = least_absolute_value_index(nums)
        l = i - 1
        answ = [0] * len(nums)
        j = 0
        while j < len(nums):
            if i < len(nums) and l >= 0:
                if abs(nums[i]) < abs(nums[l]):
                    answ[j] = nums[i] ** 2
                    i += 1
                else:
                    answ[j] = nums[l] ** 2
                    l -= 1
            elif i < len(nums):
                answ[j] = nums[i] ** 2
                i += 1
            else:
                answ[j] = nums[l] ** 2
                l -= 1
            j += 1
        return answ
