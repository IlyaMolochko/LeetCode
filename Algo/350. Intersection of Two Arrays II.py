class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answ = []
        cnt = Counter(nums1)
        for num in nums2:
            if cnt[num] > 0:
                answ.append(num)
                cnt[num] -= 1
        return answ
        
