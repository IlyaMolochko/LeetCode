class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        s = 0
        dct[0] = -1
        answ = 0
        for i in range(len(nums)):
            s += (1 if nums[i] == 1 else -1)
            if s in dct:
                answ = max(answ, i - dct[s])
            else:
                dct[s] = i
        return answ
