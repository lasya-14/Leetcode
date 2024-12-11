class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                p.append(nums1[i])
            else:
                continue
        s=set(p)
        return list(s)

        