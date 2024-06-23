class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()
        l = 0
        answ = 0
        for r in range(len(nums)):
            while mx and mx[-1] < nums[r]:
                mx.pop()
            mx.append(nums[r])
            while mn and mn[-1] > nums[r]:
                mn.pop()
            mn.append(nums[r])

            while mx[0] - mn[0] > limit:
                if mx[0] == nums[l]:
                    mx.popleft()
                if mn[0] == nums[l]:
                    mn.popleft()
                l += 1
            answ = max(answ, r - l + 1)
        return answ
