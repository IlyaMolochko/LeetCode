class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dct = defaultdict(int)
        s = 0
        dct[0] = 1
        answ = 0
        for num in nums:
            s += num
            r = s % k
            r = r if r >= 0 else r + k
            answ += dct[r]
            dct[r] += 1
        return answ
