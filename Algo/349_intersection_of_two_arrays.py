class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        answ = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            while p1 + 1 < len(nums1) and nums1[p1] == nums1[p1 + 1]:
                p1 += 1
            while p2 + 1 < len(nums2) and nums2[p2] == nums2[p2 + 1]:
                p2 += 1
            if nums1[p1] == nums2[p2]:
                answ.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return answ
