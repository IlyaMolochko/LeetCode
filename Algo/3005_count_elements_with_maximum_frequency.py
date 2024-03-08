class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)
        max_frequency = 0
        answ = 0
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] > max_frequency:
                max_frequency = frequencies[num]
                answ = frequencies[num]
            elif frequencies[num] == max_frequency:
                answ += frequencies[num]
        
        return answ
