class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        res=[-1]*len(nums)
        for t in range(2):
            for i in range(len(nums)):
                while st and nums[i]>nums[st[-1]]:
                    res[st.pop()]=nums[i]
                st.append(i)
        return res

        