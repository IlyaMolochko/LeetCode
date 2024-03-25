class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answ = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                answ.append(j + 1)
            else:
                nums[j] = -nums[j]
        return answ
