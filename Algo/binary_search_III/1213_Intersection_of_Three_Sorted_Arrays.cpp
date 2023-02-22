class Solution:
    def binary_search(self, nums: List[int], target: int):
        l = -1
        r = len(nums)
        while r - l > 1:
            x = (l + r) // 2
            if nums[x] > target:
                r = x
            elif nums[x] < target:
                l = x
            else:
                return True
        return False

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        answ = []
        for i in range(len(arr1)):
            if self.binary_search(arr2, arr1[i]) and self.binary_search(arr3, arr1[i]):
                answ.append(arr1[i])
        return answ
