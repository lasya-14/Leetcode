class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
        return list(set(res))
       

        