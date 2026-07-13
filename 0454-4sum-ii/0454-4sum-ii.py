class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1={}
        d2={}
        for i in nums1:
            for j in nums2:
                d1[i+j]=d1.get(i+j,0)+1
        for i in nums3:
            for j in nums4:
                d2[i+j]=d2.get(i+j,0)+1
        c=0
        for i in d1:
            if -i in d2:
                c+=d1[i]*d2[-i]
                d1[i]=0
        return c