class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        nums.sort(key=lambda x: (c[x], -x))
        return nums
