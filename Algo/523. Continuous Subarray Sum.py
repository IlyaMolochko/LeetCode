class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dct = defaultdict(int)
        s = 0
        dct[0] = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s % k) not in dct:
                dct[s % k] = i + 1
            elif dct[s % k] < i:
                return True
        return False
