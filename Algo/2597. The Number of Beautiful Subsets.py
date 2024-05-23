class Solution:
    def solve(self, nums, diff, cntr, i):
        if i == len(nums):
            return 1
        
        cnt = self.solve(nums, diff, cntr, i + 1)
        if nums[i] - diff not in cntr:
            cntr[nums[i]] += 1
            cnt += self.solve(nums, diff, cntr, i + 1)
            cntr[nums[i]] -= 1

            if cntr[nums[i]] == 0:
                del cntr[nums[i]]
        return cnt

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cntr = defaultdict(int)
        nums.sort()
        return self.solve(nums, k, cntr, 0) - 1
